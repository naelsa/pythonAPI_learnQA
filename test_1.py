import requests

payload = {"name": "User"}
r = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
print(r.text)