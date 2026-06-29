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
    handshake_complete = False

    print(f"\n[HANDSHAKE] Client {addr} connected.", flush=True)
    print("[HANDSHAKE] Waiting for SYN...", flush=True)

    data = client_socket.recv(1024)

    if not data:
        client_socket.close()
        continue

    command = data.decode().strip().split(" ", 1)[0]

    if command != "SYN":
        print(f"[HANDSHAKE] Expected SYN but received '{command}'", flush=True)
        client_socket.sendall(b"ERROR: EXPECTED SYN")
        client_socket.close()
        continue

    print("[HANDSHAKE] Received SYN", flush=True)
    print("[HANDSHAKE] Sending SYN-ACK", flush=True)

    client_socket.sendall(b"SYN-ACK")

    print("[HANDSHAKE] Waiting for ACK...", flush=True)

    data = client_socket.recv(1024)

    if not data:
        client_socket.close()
        continue

    command = data.decode().strip().split(" ", 1)[0]

    if command != "ACK":
        print(f"[HANDSHAKE] Expected ACK but received '{command}'", flush=True)
        client_socket.sendall(b"ERROR: EXPECTED ACK")
        client_socket.close()
        continue

    handshake_complete = True

    print("[HANDSHAKE] Received ACK", flush=True)
    print("[HANDSHAKE] Session Established", flush=True)

    client_socket.sendall(b"SESSION ESTABLISHED")

    print(f"[SERVER] Client connected: {addr}", flush=True)

    while handshake_complete:
        data = client_socket.recv(1024)

        if not data:
            print("[SERVER] Client disconnected.", flush=True)
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
            client_socket.sendall(response.encode())
            print("[SERVER] Client requested disconnect.", flush=True)
            break

        else:
            response = "ERROR: UNKNOWN COMMAND"

        print(f"[SERVER] Sending: {response}", flush=True)
        client_socket.sendall(response.encode())

    client_socket.close()