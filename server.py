from http.server import HTTPServer, SimpleHTTPRequestHandler


class MyHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Content-Security-Policy",
                         "script-src 'self' 'unsafe-inline'")
        SimpleHTTPRequestHandler.end_headers(self)


def run(server_class=HTTPServer, handler_class=MyHandler, addr="192.168.10.81", port=8001):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
