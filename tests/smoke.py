"""Exercise the built CLI against a local API without real credentials."""

import json
import errno
import os
import select
from pathlib import Path
import subprocess
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class Handler(BaseHTTPRequestHandler):
    calls = []
    fail_page = None

    def do_GET(self):
        assert self.path.startswith("/accounts"), self.path
        assert self.headers["Authorization"] == "Bearer cli-smoke-test"
        denied = "limit=1" in self.path
        response = {"message": "Fixture access denied"} if denied else {
            "data": [{"id": "account-1", "name": "Example", "custom_fields": {"nested": {"value": "preserved"}}}],
            "pagination": {"cursor": "next-page"},
            "request_id": "format-test",
        }
        payload = json.dumps(response).encode()
        self.send_response(403 if denied else 200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_POST(self):
        assert self.path == "/issues/search", self.path
        assert self.headers["Authorization"] == "Bearer cli-smoke-test"
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        assert body["filter"]["value"] == "waiting_on_customer"
        page = int(body.get("cursor") or 1)
        self.calls.append(page)
        failed = page == self.fail_page
        response = {"message": "Fixture page failed"} if failed else {
            "data": [{"id": str(page)}],
            "pagination": {"cursor": str(page + 1) if page < 11 else None},
            "request_id": "smoke-test",
        }
        payload = json.dumps(response).encode()
        self.send_response(400 if failed else 200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, *_args):
        pass


binary = Path(os.environ.get("PYLON_BINARY", "target/debug/pylon")).resolve()
server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
threading.Thread(target=server.serve_forever, daemon=True).start()


def run(*args, terminal=False, output_env=None, check=True):
    # Isolate startup from any .env file in the caller's working directory.
    with tempfile.TemporaryDirectory() as cwd:
        env = {**os.environ, "PYLON_TOKEN": "cli-smoke-test"}
        env.pop("PYLON_OUTPUT", None)
        if output_env is not None:
            env["PYLON_OUTPUT"] = output_env
        if terminal:
            master, slave = os.openpty()
            try:
                result = subprocess.run(
                    [str(binary), *args], cwd=cwd, env=env,
                    stdout=slave, stderr=subprocess.PIPE, text=True,
                    check=check, timeout=30,
                )
                chunks = []
                while select.select([master], [], [], 0.1)[0]:
                    try:
                        chunk = os.read(master, 65536)
                    except OSError as error:
                        if error.errno == errno.EIO:
                            break
                        raise
                    if not chunk:
                        break
                    chunks.append(chunk)
                result.stdout = b"".join(chunks).decode()
            finally:
                os.close(slave)
                os.close(master)
        else:
            result = subprocess.run(
                [str(binary), *args], cwd=cwd, env=env,
                capture_output=True, text=True, check=check, timeout=30,
            )
        return result


try:
    accounts = ("accounts", "list", "--base-url", f"http://127.0.0.1:{server.server_port}", "--limit", "5", "--no-pager")
    for terminal in ([False, True] if os.name != "nt" else [False]):
        result = run(*accounts, terminal=terminal)
        response = json.loads(result.stdout)
        assert response["data"][0]["custom_fields"]["nested"]["value"] == "preserved"
        assert response["pagination"]["cursor"] == "next-page"
        assert response["request_id"] == "format-test"
        assert not result.stderr, result.stderr
        denied_args = list(accounts)
        denied_args[denied_args.index("--limit") + 1] = "1"
        denied = run(*denied_args, terminal=terminal, check=False)
        assert denied.returncode != 0
        assert json.loads(denied.stdout)["error"]["code"] == 403, denied.stdout
    for override in [("--format", "table"), ("--human",)]:
        table = run(*accounts, *override)
        assert "Example" in table.stdout and not table.stdout.lstrip().startswith("{")
    table = run(*accounts, output_env="table")
    assert "Example" in table.stdout and not table.stdout.lstrip().startswith("{")
    assert json.loads(run(*accounts, "--format", "json", output_env="table").stdout)["request_id"] == "format-test"

    search = (
        "issues", "search", "--base-url", f"http://127.0.0.1:{server.server_port}",
        "--json", '{"filter":{"field":"state","operator":"equals","value":"waiting_on_customer"}}',
        "--page-all", "--page-delay", "0", "--no-pager", "--format", "jsonl",
    )
    capped = run(*search, "--page-limit", "10")
    pages = [json.loads(line) for line in capped.stdout.splitlines()]
    assert len(pages) == 10, pages
    assert pages[-1]["pagination"]["cursor"] == "11"
    assert Handler.calls == list(range(1, 11)), Handler.calls
    assert "Output is incomplete" in capped.stderr, capped.stderr

    Handler.calls.clear()
    complete = run(*search)
    pages = [json.loads(line) for line in complete.stdout.splitlines()]
    assert len(pages) == 11, pages
    assert pages[-1]["pagination"]["cursor"] is None
    assert Handler.calls == list(range(1, 12)), Handler.calls
    assert not complete.stderr, complete.stderr

    exact = run(*search, "--page-limit", "11")
    assert not exact.stderr, exact.stderr

    limited_projection = run(*search, "--page-limit", "2", "--query", "[].data[]")
    assert len(limited_projection.stdout.splitlines()) == 2
    assert "Output is incomplete" in limited_projection.stderr

    invalid = run(*search, "--page-limit", "0", check=False)
    assert invalid.returncode != 0

    Handler.calls.clear()
    Handler.fail_page = 3
    failed = run(*search, check=False)
    assert failed.returncode != 0
    assert Handler.calls == [1, 2, 3], Handler.calls
    error = json.loads(failed.stdout.splitlines()[-1])
    assert error["error"]["code"] == 400, error
    Handler.fail_page = None

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
    print("CLI smoke checks passed: JSON defaults, full responses, format overrides, errors, pagination, projection, and dry-run")
finally:
    server.shutdown()
    server.server_close()
