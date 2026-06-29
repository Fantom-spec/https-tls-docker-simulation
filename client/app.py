import socket
import json
import time

HOST = "server"      # Docker service name
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        client.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")
        break
    except ConnectionRefusedError:
        print("Server not ready. Retrying in 2 seconds...")
        time.sleep(2)

while True:
    try:
        name = input("Enter name: ")
        message = input("Enter message: ")

        msg = {
            "name": name,
            "message": message
        }

        client.sendall(json.dumps(msg).encode())

        response = client.recv(1024)

        if not response:
            print("Server disconnected.")
            break

        data = json.loads(response.decode())

        print("\nServer Response:")
        print(json.dumps(data, indent=4))

    except KeyboardInterrupt:
        print("\nClosing client...")
        break

client.close()