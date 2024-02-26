#!/usr/bin/python3

"""
Prints the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    """

    if not subreddit or not isinstance(subreddit, str):
        print("Subreddit name must be a non-empty string.")
        return

    user_agent = {'User-agent': 'Your Bot 1.0'}
    params = {'limit': 10}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    try:
        response = requests.get(url, headers=user_agent, params=params)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        results = response.json()
        for post in results.get('data', {}).get('children', []):
            print(post.get('data', {}).get('title'))
    except requests.RequestException as e:
        print(f"Error fetching subreddit data: {e}")
        return

# Example usage
subreddit_name = "python"
print(f"Top 10 hot posts in r/{subreddit_name}:")
top_ten(subreddit_name)
