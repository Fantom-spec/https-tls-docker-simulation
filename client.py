import time
import requests
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CA_PATH = os.path.join(BASE_DIR, "certs", "ca.crt")

SERVER_URL = "https://localhost:8443"

print("----------------------------------------")
print(" HTTPS Client Started")
print("----------------------------------------")

time.sleep(2)

while True:
    try:
        print("\nConnecting to server...")

        print("Using CA:", CA_PATH)

        response = requests.get(
            f"{SERVER_URL}/hello",
            verify=False,
            timeout=5
        )

        print(f"Status Code : {response.status_code}")
        print(f"Response    : {response.text.strip()}")

    except requests.exceptions.SSLError as e:
        print(f"TLS Error: {e}")

    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error: {e}")

    except Exception as e:
        print(f"Error: {e}")

    time.sleep(5)