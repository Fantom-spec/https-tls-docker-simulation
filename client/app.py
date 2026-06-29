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

print("[CLIENT] Connected")

print("[HANDSHAKE] Sending SYN")
client.sendall(b"SYN")

response = client.recv(1024).decode().strip()

if response != "SYN-ACK":
    print(f"[HANDSHAKE] Failed: {response}")
    client.close()
    exit(1)

print("[HANDSHAKE] Received SYN-ACK")
print("[HANDSHAKE] Sending ACK")

client.sendall(b"ACK")

response = client.recv(1024).decode().strip()

if response != "SESSION ESTABLISHED":
    print(f"[HANDSHAKE] Failed: {response}")
    client.close()
    exit(1)

print("[HANDSHAKE] Session Established")

while True:
    command = input("> ").strip()

    if command == "":
        continue

    try:
        client.sendall(command.encode())

        response = client.recv(1024)

        if not response:
            print("[CLIENT] Server disconnected.")
            break

        print("[SERVER]", response.decode())

        if command.upper() == "EXIT":
            break

    except Exception as e:
        print(f"[CLIENT] Error: {e}")
        break

client.close()

print("[CLIENT] Connection closed.")