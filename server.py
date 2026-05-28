from http.server import HTTPServer, BaseHTTPRequestHandler
import os

if not os.path.exists("status.txt"):
    with open("status.txt", "w") as f:
        f.write("OFF")

def updateStatus(new_status):
    with open("status.txt", "w") as data_base:
        data_base.write(new_status)

def readStatus():
    with open("status.txt", "r") as data_base:
        return data_base.read()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        if self.path == '/status-on':
            updateStatus('ON')
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Status changed')
        
        elif self.path == '/status-off':
            updateStatus('OFF')
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Status changed')
        
        else:
            self.send_response(200)
            self.end_headers()
            status = readStatus()
            self.wfile.write(f'STATUS: {status}'.encode())

print('Сервер запущен: http://localhost:3000')
HTTPServer(('localhost', 3000), Handler).serve_forever()