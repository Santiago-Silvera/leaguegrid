from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve the main HTML file
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            with open("index.html", "r", encoding="utf-8") as file:
                self.wfile.write(file.read().encode("utf-8"))
        
        # Serve static files (like images and JavaScript)
        elif self.path.endswith(".js"):
            try:
                file_path = self.path.lstrip("/")  # Remove the leading slash
                if os.path.exists(file_path):
                    self.send_response(200)
                    self.send_header("Content-Type", "application/javascript")
                    self.end_headers()
                    with open(file_path, "rb") as file:
                        self.wfile.write(file.read())
                else:
                    self.send_response(404)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "File not found"}).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
        
        # Serve other static files (like images)
        elif self.path.endswith(".png"):
            try:
                file_path = self.path.lstrip("/")  # Remove the leading slash
                if os.path.exists(file_path):
                    self.send_response(200)
                    self.send_header("Content-Type", "image/png")
                    self.end_headers()
                    with open(file_path, "rb") as file:
                        self.wfile.write(file.read())
                else:
                    self.send_response(404)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "File not found"}).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))

        # Handle other requests (return JSON)
        else:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {}
            self.wfile.write(json.dumps(response).encode("utf-8"))

if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Server running on port 8000...")
    httpd.serve_forever()
