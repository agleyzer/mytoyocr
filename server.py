#!/usr/bin/python3

import http.server
import socketserver
import json
from urllib import request

PORT = 8000

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('content-length'))
        
        input = json.loads(self.rfile.read(length))
    
        with request.urlopen(input['imgBase64']) as r:
            data = r.read()
            with open("/tmp/image.png", "wb") as f:
                f.write(data)

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