#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""
import requests
from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    # if subreddit is None or not isinstance(subreddit, str):
    #     return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=user_agent)
    results = response.json()
    # print(response.content)
    # print(response.encoding.)
    # print(results.get("data").get("subscribers"))

    try:
        print(results.get("data").get("subscribers"))

    except Exception:("what the fuck")
       



number_of_subscribers("learnpython")