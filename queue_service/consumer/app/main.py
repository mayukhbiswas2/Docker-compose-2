import time
import json
import requests
from redis_client import redis_client

FLASK_ENDPOINT = "http://flask_app:5000/process_data"

def process_data():
    while True:
        # Fetch data from the queue
        data = redis_client.lpop("data_queue")
        if data:
            payload = json.loads(data)
            try:
                # Send data to Flask service
                response = requests.post(FLASK_ENDPOINT, json=payload)
                print(f"Sent to Flask: {payload} - Response: {response.status_code}")
            except Exception as e:
                print(f"Error sending data to Flask: {e}")
        time.sleep(1)

if __name__ == "__main__":
    process_data()
