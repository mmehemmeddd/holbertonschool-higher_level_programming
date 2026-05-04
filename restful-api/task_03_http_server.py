from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPI(BaseHTTPRequestHandler):

    def do_GET(self):

        # root endpoint
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # data endpoint
        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        # status endpoint (ÇOX VACİB FIX BURADADIR)
        elif self.path == "/status":
            data = {"status": "OK"}

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        # undefined endpoint
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPI, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)

    print("Server running on port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()c
