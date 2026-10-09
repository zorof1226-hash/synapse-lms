import os
import requests
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("GEMINI_API_KEY", "")
print(f"Key: {key[:30]}...")

# Try listing models to see what's available
models_url = f"https://generativelanguage.googleapis.com/v1beta/models?key={key}"
resp = requests.get(models_url, timeout=15)
print(f"List models status: {resp.status_code}")
if resp.status_code == 200:
    data = resp.json()
    for m in data.get("models", [])[:10]:
        print(f"  - {m.get('name')}: {m.get('displayName')}")
else:
    print(f"Error: {resp.text[:400]}")

# Try gemini-2.0-flash
print("\n--- Trying gemini-2.0-flash ---")
url2 = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={key}"
payload = {"contents": [{"parts": [{"text": "What is 2+2?"}]}]}
resp2 = requests.post(url2, json=payload, timeout=20)
print(f"Status: {resp2.status_code}")
print(f"Response: {resp2.text[:400]}")
