import json
import requests
from datetime import datetime, timezone
from pathlib import Path

#  CORRECT API URL FROM README
API_URL = "https://jsonplaceholder.typicode.com/posts"

print("REST API INSPECTION")
print("="*50)

try:
    response = requests.get(API_URL, timeout=20)
    print(f"Status: {response.status_code}")
    print(f"Content-Type: {response.headers.get('Content-Type')}")
    
    payload = response.json()
    print(f"Structure: {type(payload).__name__}")
    
    if isinstance(payload, list):
        print(f"Records: {len(payload)}")
        if len(payload) > 0:
            print(f"\nSample Record:")
            print(json.dumps(payload[0], indent=2))
    
    with open("data/raw/api_snapshot.json", "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    
    timestamp = datetime.now(timezone.utc).isoformat()
    print(f"\nSaved to: data/raw/api_snapshot.json")
    print(f"Retrieved at (UTC): {timestamp}")
    
except Exception as e:
    print(f"Error: {e}")