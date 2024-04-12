import urllib
from urllib import parse, request

response = request.urlopen("http://localhost")
# print(response.url)

params = {'v':'LosiGgon_KM'}
query = parse.urlencode(params)

url = "https://www.youtube.com/watch" + "?"+ query
resp = request.urlopen(url)
print(resp.code)
html = resp.read().decode("utf-8")
print(type(html))
print(html[:100])