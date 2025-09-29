# client.py
import requests
import sys

# Usage: python client.py [BASE_URL]
# Example: python client.py http://localhost:8080
BASE_URL = (sys.argv[1].rstrip('/') if len(sys.argv) > 1 else "http://localhost:8080")

TIMEOUT_SECONDS = 2  # Step 4 requirement

def call(endpoint, x, y):
    url = f"{BASE_URL}{endpoint}"
    try:
        resp = requests.post(url, json={"x": x, "y": y}, timeout=TIMEOUT_SECONDS)
        resp.raise_for_status()
        data = resp.json()
        print(f"{endpoint.strip('/')}({x},{y}) = {data.get('result')}")
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.RequestException as e:
        # other network errors / HTTP errors
        print("Request failed:", e)
    except ValueError:
        print("Invalid JSON response")

def main():
    call("/add", 2, 3)
    call("/multiply", 4, 5)

if __name__ == "__main__":
    main()
