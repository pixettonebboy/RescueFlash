# start_server.py
import http.server
import socketserver
import webbrowser
import threading
import os

PORT = 8000

def run_server():
    os.chdir(os.path.dirname(__file__))  # Serve dalla directory dello script
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        webbrowser.open(f"http://localhost:{PORT}")
        httpd.serve_forever()

thread = threading.Thread(target=run_server)
thread.start()
