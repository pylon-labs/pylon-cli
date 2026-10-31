"""Regression checks with fake credentials and a local API only."""

import json
import os
from pathlib import Path
import select
import subprocess
import tempfile
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


binary = Path(os.environ.get("PYLON_BINARY", "target/debug/pylon")).resolve()
env = {**os.environ, "PYLON_TOKEN": "FAKE_PYLON_SECURITY_TOKEN", "FERN_CLI_CREDENTIAL_STORE": "file"}
env.pop("PYLON_LOG_FILE", None)
env.pop("PYLON_LOG", None)
title = "normal\x1b[2J\u202espoof"


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        assert self.path == "/issues/search"
        assert self.headers["Authorization"] == "Bearer FAKE_PYLON_SECURITY_TOKEN"
        self.rfile.read(int(self.headers.get("Content-Length", 0)))
        payload = json.dumps({"data": [{"id": "1", "title": title}], "pagination": {"cursor": None}, "request_id": "test"}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, *_args):
        pass


server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
threading.Thread(target=server.serve_forever, daemon=True).start()

try:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)

        def run(*args):
            result = subprocess.run([str(binary), *args], cwd=root, env=env,
                                    capture_output=True, timeout=15)
            assert result.returncode == 0, (result.stdout + result.stderr).decode()
            return result

        base = f"http://127.0.0.1:{server.server_port}"
        search = ("issues", "search", "--base-url", base)
        table = run(*search, "--format", "table")
        assert b"\x1b" not in table.stdout and "\u202e".encode() not in table.stdout
        machine = json.loads(run(*search, "--format", "json").stdout)
        assert machine["data"][0]["title"] == title
        debug = run(*search, "--debug")
        assert b"FAKE_PYLON_SECURITY_TOKEN" not in debug.stdout + debug.stderr

        fake_file = root / "fake-local-file.txt"
        fake_file.write_text("FAKE_LOCAL_FILE_CONTENT")
        for value in (f"@{fake_file}", f"@file://{fake_file}", f"@data://{fake_file}", r"\@literal"):
            payload = {"body_html": value, "message_id": "00000000-0000-0000-0000-000000000002"}
            request = run("issues", "reply", "--issue-id", "00000000-0000-0000-0000-000000000001",
                          "--json", json.dumps(payload), "--dry-run")
            assert json.loads(request.stdout)["body"]["body_html"] == value
        filter_value = {"field": "title", "operator": "equals", "value": f"@{fake_file}"}
        request = run(*search, "--filter", json.dumps(filter_value), "--dry-run")
        assert json.loads(request.stdout)["body"]["filter"]["value"] == f"@{fake_file}"

        logs = root / "unexpected-logs"
        (root / ".env").write_text(f"PYLON_LOG_FILE={logs}\nLD_PRELOAD=/fake/attacker-library.so\n")
        run(*search)
        assert not logs.exists(), "An untrusted .env configured the CLI process"

        if os.name == "posix":
            import pty
            import signal
            import termios

            def drain(fd, duration):
                output = b""
                until = time.monotonic() + duration
                while time.monotonic() < until:
                    if select.select([fd], [], [], 0.05)[0]:
                        try:
                            output += os.read(fd, 65536)
                        except OSError:
                            break
                return output

            master, slave = pty.openpty()
            proc = subprocess.Popen([str(binary), "auth", "login", "--with-token"], cwd=root, env=env,
                                    stdin=slave, stdout=slave, stderr=slave)
            try:
                prompt = drain(master, 1.5)
                assert b"Paste your token" in prompt
                assert not termios.tcgetattr(slave)[3] & termios.ECHO
                marker = b"FAKE_TOKEN_MUST_NOT_ECHO"
                os.write(master, marker)
                assert marker not in drain(master, 0.3)
                # Erase the fake input and submit empty input, before any storage.
                os.write(master, b"\x15\n")
                drain(master, 0.5)
                proc.wait(timeout=5)
                assert termios.tcgetattr(slave)[3] & termios.ECHO
            finally:
                if proc.poll() is None:
                    proc.kill()
                    proc.wait(timeout=5)
                os.close(master)
                os.close(slave)

            for interruption in (signal.SIGINT, signal.SIGTERM):
                master, slave = pty.openpty()
                proc = subprocess.Popen([str(binary), "auth", "login", "--with-token"], cwd=root, env=env,
                                        stdin=slave, stdout=slave, stderr=slave)
                try:
                    assert b"Paste your token" in drain(master, 1.5)
                    assert not termios.tcgetattr(slave)[3] & termios.ECHO
                    os.kill(proc.pid, interruption)
                    proc.wait(timeout=5)
                    assert termios.tcgetattr(slave)[3] & termios.ECHO
                finally:
                    if proc.poll() is None:
                        proc.kill()
                        proc.wait(timeout=5)
                    os.close(master)
                    os.close(slave)

        print("Security checks passed: literal JSON, sanitized tables, ignored .env, and hidden token input")
finally:
    server.shutdown()
    server.server_close()
