#!/usr/bin/python3
"""
number of subscribers for a given Subreddit
"""
import requests


# from requests import get


def number_of_subscribers(Subreddit):
    """
    function that queries the    Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given Subreddit.
    """
    if Subreddit is None or not isinstance(Subreddit, str):
        return 0

    user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                                '(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(Subreddit)
    response = requests.get(url)
    results = response.json()

    # print(response.content)
    # print(response.encoding.)
    # print(results.get("data").get("subscribers"))

    return results.get("data").get("subscribers")


print(number_of_subscribers("learnpython"))

