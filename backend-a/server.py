#!/usr/bin/env python3
import hashlib
import json
import socket
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

BACKEND = "A"
PORT = 3001
CACHE_BODY = json.dumps({"backend": BACKEND, "resource": "cache"}).encode()
CACHE_ETAG = '"' + hashlib.sha256(CACHE_BODY).hexdigest()[:16] + '"'


class Handler(BaseHTTPRequestHandler):
    def respond(self, status, body=b"", content_type="application/json", headers=None):
        self.send_response(status)
        self.send_header("X-Backend", BACKEND)
        for name, value in (headers or {}).items():
            self.send_header(name, value)
        if status != 304:
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if body and status != 304 and self.command != "HEAD":
            self.wfile.write(body)

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path == "/":
            body = json.dumps({"backend": BACKEND, "status": "ok"}).encode()
            self.respond(200, body, headers={"Cache-Control": "no-store"})
        elif path == "/api/status":
            body = json.dumps({"backend": BACKEND, "status": "ok", "host": socket.gethostname()}).encode()
            self.respond(200, body, headers={"Cache-Control": "no-store"})
        elif path == "/api/cache":
            headers = {"Cache-Control": "max-age=60", "ETag": CACHE_ETAG}
            if self.headers.get("If-None-Match") == CACHE_ETAG:
                self.respond(304, headers=headers)
            else:
                self.respond(200, CACHE_BODY, headers=headers)
        else:
            self.respond(404, json.dumps({"error": "not found"}).encode())

    do_HEAD = do_GET


ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
