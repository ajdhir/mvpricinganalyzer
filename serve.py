#!/usr/bin/env python3
"""Simple HTTP server to serve the Vehicle MAP Price Analyzer.

Binds to 0.0.0.0 so the app is accessible from any network interface.

Usage:
    python3 serve.py [port]

Default port is 8080.
"""

import http.server
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
HOST = "0.0.0.0"

handler = http.server.SimpleHTTPRequestHandler
server = http.server.HTTPServer((HOST, PORT), handler)

print(f"Serving on http://{HOST}:{PORT}")
print(f"Access from your browser: http://108.174.103.202:{PORT}")
print("Press Ctrl+C to stop.")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
    server.server_close()
