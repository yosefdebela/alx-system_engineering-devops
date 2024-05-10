#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about/.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=True)
    # print(response.json())
    if response.status_code == 200:
        data = response.json()
        sub = data["data"]["children"][0]["data"]["subscribers"]
        return sub
    else:
        return 0

    