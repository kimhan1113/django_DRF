import requests


token = ""

headers = {
    'Authorization': f"Token {token}"
}

res = requests.get("http://localhost:8000/post/1/", headers=headers)
print(res.json())