import http.server
import socketserver
import base64
import os
from functools import partial

USERNAME = os.getenv("DASHBOARD_USER", "admin")
PASSWORD = os.getenv("DASHBOARD_PASSWORD", "aitrader2025")

class AuthHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm="AI-Trader Dashboard"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        auth_header = self.headers.get('Authorization')
        if auth_header is None:
            self.do_AUTHHEAD()
            self.wfile.write(b'Authentication required')
            return
        
        auth_decoded = base64.b64decode(auth_header.split(' ')[1]).decode('utf-8')
        username, password = auth_decoded.split(':', 1)
        
        if username == USERNAME and password == PASSWORD:
            super().do_GET()
        else:
            self.do_AUTHHEAD()
            self.wfile.write(b'Invalid credentials')

if __name__ == '__main__':
    PORT = int(os.getenv("PORT", 8888))
    os.chdir('docs')
    
    with socketserver.TCPServer(("", PORT), AuthHTTPRequestHandler) as httpd:
        print(f"Dashboard with auth running on port {PORT}")
        print(f"Username: {USERNAME}")
        print(f"Password: {PASSWORD}")
        httpd.serve_forever()
