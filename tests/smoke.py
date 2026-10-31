"""Exercise the built CLI against a local API without real credentials."""

import json
import os
from pathlib import Path
import subprocess
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class Handler(BaseHTTPRequestHandler):
    calls = []

    def do_POST(self):
        assert self.path == "/issues/search", self.path
        assert self.headers["Authorization"] == "Bearer cli-smoke-test"
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        assert body["filter"]["value"] == "waiting_on_customer"
        page = int(body.get("cursor") or 1)
        self.calls.append(page)
        response = {
            "data": [{"id": str(page)}],
            "pagination": {"cursor": str(page + 1) if page < 11 else None},
            "request_id": "smoke-test",
        }
        payload = json.dumps(response).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, *_args):
        pass


binary = Path(os.environ.get("PYLON_BINARY", "target/debug/pylon")).resolve()
server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
threading.Thread(target=server.serve_forever, daemon=True).start()


def run(*args):
    # Isolate startup from any .env file in the caller's working directory.
    with tempfile.TemporaryDirectory() as cwd:
        result = subprocess.run(
            [str(binary), *args],
            cwd=cwd,
            env={**os.environ, "PYLON_TOKEN": "cli-smoke-test"},
            capture_output=True,
            text=True,
            check=True,
            timeout=30,
        )
        return result


try:
    search = (
        "issues", "search", "--base-url", f"http://127.0.0.1:{server.server_port}",
        "--json", '{"filter":{"field":"state","operator":"equals","value":"waiting_on_customer"}}',
        "--page-all", "--page-delay", "0", "--no-pager", "--format", "jsonl",
    )
    capped = run(*search)
    pages = [json.loads(line) for line in capped.stdout.splitlines()]
    assert len(pages) == 10, pages
    assert pages[-1]["pagination"]["cursor"] == "11"
    assert Handler.calls == list(range(1, 11)), Handler.calls
    assert not capped.stderr, capped.stderr

    Handler.calls.clear()
    complete = run(*search, "--page-limit", "12")
    pages = [json.loads(line) for line in complete.stdout.splitlines()]
    assert len(pages) == 11, pages
    assert pages[-1]["pagination"]["cursor"] is None
    assert Handler.calls == list(range(1, 12)), Handler.calls

    Handler.calls.clear()
    resumed_search = list(search)
    initial_body = json.loads(resumed_search[resumed_search.index("--json") + 1])
    initial_body["cursor"] = "5"
    resumed_search[resumed_search.index("--json") + 1] = json.dumps(initial_body)
    resumed = run(*resumed_search, "--page-limit", "12")
    assert Handler.calls == list(range(5, 12)), Handler.calls
    assert len(resumed.stdout.splitlines()) == 7

    projected = run(*search, "--page-limit", "12", "--query", "[].data[]")
    rows = [json.loads(line) for line in projected.stdout.splitlines()]
    assert [row["id"] for row in rows] == [str(i) for i in range(1, 12)]

    calls_before = len(Handler.calls)
    dry_run = json.loads(run(
        "issues", "bulk-update", "--dry-run", "--json",
        '{"issue_ids":["00000000-0000-0000-0000-000000000001"],"state":"closed"}',
    ).stdout)
    assert dry_run["method"] == "PATCH", dry_run
    assert dry_run["body"]["state"] == "closed", dry_run
    assert len(Handler.calls) == calls_before
    print("CLI smoke checks passed: pagination cap, full export, projection, and bulk-update dry-run")
finally:
    server.shutdown()
    server.server_close()
