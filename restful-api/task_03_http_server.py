import http.server
import json

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        # ── 1. KÖK ENDPOİNT: GET / ──────────────────────────────
        if self.path == "/":
            self.send_response(200)                        # 200 OK statusu
            self.send_header("Content-type", "text/plain") # Mətn cavabı
            self.end_headers()                             # Başlıqları bitir
            self.wfile.write(b"Hello, this is a simple API!")  # Cavabı göndər

        # ── 2. DATA ENDPOİNTİ: GET /data ────────────────────────
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")  # JSON cavabı
            self.end_headers()
            
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)                   # dict → JSON string
            self.wfile.write(json_data.encode("utf-8"))    # Göndər

        # ── 3. STATUS ENDPOİNTİ: GET /status ────────────────────
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # ── 4. INFO ENDPOİNTİ: GET /info ────────────────────────
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode("utf-8"))

        # ── 5. TАПILMAYAN ENDPOİNT → 404 ────────────────────────
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run():
    server_address = ("", 8000)   # bütün interfeyslər, port 8000
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print("Server running on port 8000...")
    httpd.serve_forever()         # serveri işə sal


if __name__ == "__main__":
    run()
