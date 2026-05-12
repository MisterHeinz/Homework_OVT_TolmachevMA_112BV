from http.server import HTTPServer, BaseHTTPRequestHandler

status = 'OFF'

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global status
        
        if self.path == '/status-on':
            status = 'ON'
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')
        
        elif self.path == '/status-off':
            status = 'OFF'
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')
        
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(f'STATUS: {status}'.encode())

print('Сервер запущен: http://localhost:3000')
HTTPServer(('localhost', 3000), Handler).serve_forever()