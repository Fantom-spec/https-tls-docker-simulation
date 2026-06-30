from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl


HOST = "0.0.0.0"
PORT = 8443


class HTTPSRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        print(f"[+] Received GET request from {self.client_address}")

        if self.path == "/":

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write(
                b"Hello from HTTPS Server!\n"
            )

        elif self.path == "/hello":

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write(
                b"Hello Client!\n"
            )

        elif self.path == "/status":

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write(
                b"Server is running.\n"
            )

        else:

            self.send_response(404)
            self.end_headers()

            self.wfile.write(
                b"404 Not Found\n"
            )

    def log_message(self, format, *args):
        return


httpd = HTTPServer((HOST, PORT), HTTPSRequestHandler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

context.load_cert_chain(
    certfile="certs/server.crt",
    keyfile="certs/server.key"
)

httpd.socket = context.wrap_socket(
    httpd.socket,
    server_side=True
)

print("----------------------------------------")
print(" HTTPS Server Started")
print(f" Listening on https://0.0.0.0:{PORT}")
print("----------------------------------------")

httpd.serve_forever()