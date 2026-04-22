import requests

payload = {
    "time": True,
    "continuity": True,
    "alignment": True,
    "genesis": True,
    "boundary": True,
    "reference": True,
    "causality": True,
    "consciousness": True
}

response = requests.post("http://127.0.0.1:5000/evaluate", json=payload)

print(response.status_code)
print(response.json())
