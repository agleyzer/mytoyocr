#!/usr/bin/python3

import http.server
import socketserver
import json

PORT = 8000

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('content-length'))
        
        with open('/tmp/image.png','wb') as s:
                s.write(self.rfile.read(length))

        #send response code:
        self.send_response(201)

        #send headers:
        self.send_header("Content-Type", "application/json;charset=UTF-8")
        self.end_headers()

        #send response:
        output = json.dumps({"whoa": True})
        self.wfile.write(output.encode(encoding='utf-8'))

# Create an object of the above class
handler = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Server started at localhost:" + str(PORT))
    httpd.serve_forever()