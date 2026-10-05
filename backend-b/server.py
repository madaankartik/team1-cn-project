from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from urllib.parse import urlparse

HOST = "0.0.0.0"
PORT = 3002

CACHE_ETAG = '"backend-b-v1"'


class BackendHandler(BaseHTTPRequestHandler):

    def send_json(self, data, status=200, extra_headers=None):
        body = json.dumps(data).encode("utf-8")

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Backend", "B")

        if extra_headers:
            for name, value in extra_headers.items():
                self.send_header(name, value)

        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = urlparse(self.path).path

        if path == "/":
            self.send_json({
                "message": "Backend B is running",
                "backend": "B",
                "status": "ok"
            })

        elif path == "/api/status":
            self.send_json({
                "backend": "B",
                "status": "ok"
            })

        elif path == "/api/cache":
            client_etags = [
                value.strip().removeprefix("W/")
                for value in self.headers.get("If-None-Match", "").split(",")
            ]

            if CACHE_ETAG in client_etags or "*" in client_etags:
                self.send_response(304)
                self.send_header("X-Backend", "B")
                self.send_header("ETag", CACHE_ETAG)
                self.send_header("Cache-Control", "public, max-age=60")
                self.end_headers()
                return

            self.send_json(
                {
                    "backend": "B",
                    "message": "This response is cacheable",
                    "status": "ok"
                },
                extra_headers={
                    "Cache-Control": "public, max-age=60",
                    "ETag": CACHE_ETAG
                }
            )

        else:
            self.send_json(
                {
                    "error": "Not Found",
                    "backend": "B"
                },
                status=404
            )

    def log_message(self, format, *args):
        print(
            f"[Backend B] {self.address_string()} - "
            f"{format % args}"
        )


server = ThreadingHTTPServer((HOST, PORT), BackendHandler)

print(f"Backend B running on {HOST}:{PORT}")

server.serve_forever()
