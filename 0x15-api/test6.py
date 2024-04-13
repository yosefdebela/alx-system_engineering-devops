# request.py

from urllib.error import HTTPError, URLError

from urllib.request import urlopen, Request
url = "https://www.httpbin.org/user-agent"
headers = {"user-Agent": "Real python"}

def make_request(url, headers=None):
    request = Request(url, headers=headers or {})
    try:

        with urlopen(request, timeout=10) as response:
             print(response.status)
             return response.read(), response
    except HTTPError as error:
         print(error.status, error.reason)
    except URLError as error:
         print(error.reason)
    except TimeoutError:
         print("Request timed out")

    make_request(url, headers = None)