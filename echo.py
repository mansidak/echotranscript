from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse

class EchoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        parsed_path = parse.urlparse(self.path)
        query = parse.parse_qs(parsed_path.query)

        # Extract the 'text' parameter, if it existsf
        text = query.get('text', [''])[0]  # Default to an empty string if not found

        # Set headers
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        # Write the response body
        self.wfile.write(text.encode())

def run(server_class=HTTPServer, handler_class=EchoHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
