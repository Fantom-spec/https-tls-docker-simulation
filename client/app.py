import socket

HOST = "server"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f"[CLIENT] Connecting to {HOST}:{PORT}...")

try:
    client.connect((HOST, PORT))
except Exception as e:
    print(f"[CLIENT] Connection failed: {e}")
    exit(1)

print("[CLIENT] Connected!")

while True:
    command = input("> ").strip()

    if command == "":
        continue

    try:
        client.sendall(command.encode())

        response = client.recv(1024)

        if not response:
            print("[CLIENT] Server closed the connection.")
            break

        print("[SERVER RESPONSE]", response.decode())

        if command.upper() == "EXIT":
            break

    except Exception as e:
        print(f"[CLIENT] Error: {e}")
        break

client.close()
print("[CLIENT] Connection closed.")