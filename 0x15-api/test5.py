# request.py

from urllib.error import HTTPError, URLError
from urllib.request import urlopen

url = "https://www.google.com"

def make_request(url):
    try:
        with urlopen(url, timeout=10) as response:
            print(response.status)
            return response.read(), response

    except UnicodeError as error:
        print(error)
    except HTTPError as error:
        print(error.status, error.reason)
    except URLError as error:
        print(error.reason)
    except TimeoutError:
        print("Request timed out")

make_request(url)