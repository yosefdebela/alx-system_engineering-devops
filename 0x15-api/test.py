import requests

requests.get("http://localhost/get")

requests.post("http://localhost/post", data={"key": "value"})

requests.put("http://localhost/put", data={"key": "value"})

requests.delete("http://localhost/delete")

requests.head("http://localhost/get")

requests.patch("http://localhost/patch", data={"key": "value"})

requests.options("http://localhost/get")
