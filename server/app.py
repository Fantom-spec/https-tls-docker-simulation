import socket
import json

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind((HOST, PORT))
server.listen(5)

print(f"Server listening on {HOST}:{PORT}",flush=True)

while True:
    client_socket, client_addr = server.accept()
    print(f"\nClient connected: {client_addr}")

    while True:
        try:
            data = client_socket.recv(1024)

            if not data:
                print(f"Client {client_addr} disconnected.")
                break

            message = data.decode()
            print(f"Received: {message}")

            try:
                obj = json.loads(message)

                response = {
                    "status": "ok",
                    "received": obj
                }

            except json.JSONDecodeError:
                response = {
                    "status": "error",
                    "message": "Invalid JSON"
                }

            client_socket.sendall(json.dumps(response).encode())

        except ConnectionResetError:
            print(f"Connection lost with {client_addr}",flush=True)
            break

    client_socket.close()