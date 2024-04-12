import requests


response = requests.post("https://httpbin.org/post", json={"key": "value"})
json_response = response.json()
json_response["data"]

json_response["headers"]["Content-Type"]

print(response.request)
print(requests.session)
print(response)