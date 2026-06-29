import socket

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen(5)

print(f"[SERVER] Listening on {HOST}:{PORT}", flush=True)

while True:
    client_socket, addr = server.accept()
    print(f"[SERVER] Client connected: {addr}", flush=True)

    while True:
        data = client_socket.recv(1024)

        if not data:
            print("[SERVER] Client disconnected")
            break

        message = data.decode().strip()
        print(f"[SERVER] Received: {message}", flush=True)

        parts = message.split(" ", 1)
        command = parts[0]
        payload = parts[1] if len(parts) > 1 else ""

        if command == "HELLO":
            response = f"WELCOME {payload}"

        elif command == "MSG":
            response = f"ACK: {payload}"

        elif command == "PING":
            response = "PONG"

        elif command == "EXIT":
            response = "BYE"
            client_socket.send(response.encode())
            break

        else:
            response = "ERROR: UNKNOWN COMMAND"
        
        print(f"[SERVER] Sending: {response}",flush=True)
        client_socket.send(response.encode())

    client_socket.close()