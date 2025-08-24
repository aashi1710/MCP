import sseclient
import requests

# Connect to SSE stream
print("Connecting to server...")
messages = sseclient.SSEClient("http://127.0.0.1:8000/sse")

for msg in messages:
    if msg.event == "tools":
        print("Available tools:", msg.data)

        # Test running the tools
        r1 = requests.get("http://127.0.0.1:8000/run/add", params={"a": 5, "b": 7})
        r2 = requests.get("http://127.0.0.1:8000/run/multiply", params={"a": 3, "b": 4})

        print("add(5,7) =", r1.json())
        print("multiply(3,4) =", r2.json())
        break  # stop after first response
