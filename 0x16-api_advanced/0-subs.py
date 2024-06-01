# #!/usr/bin/python3
# """
# Script that queries subscribers on a given Reddit subreddit.
# """
#
# import requests
#
#
# def number_of_subscribers(subreddit):
#     """Return the total number of subscribers on a given subreddit."""
#     url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
#     headers = {"User-Agent": "Mozilla/5.0"}
#     response = requests.get(url, headers=headers, allow_redirects=False)
#     if response.status_code == 200:
#         data = response.json()
#         subscribers = data['data']['subscribers']
#         return subscribers
#     else:
#         return 0


# from dotenv import load_dotenv
# import os
import requests
import sys
import json


# from urllib import urlopen
# from urllib import parse

# subreddit = sys.argv[1]

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # load_dotenv()
    # cid = os.getenv("client2ID")
    # sid = os.getenv("secret2")
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    data = response.json()
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <subreddit>".format(sys.argv[0]))
        sys.exit(1)
    subreddit = sys.argv[1]
    print("Subreddit: {}".format(subreddit))
    print("Number of subscribers: {}".format(number_of_subscribers(subreddit)))


