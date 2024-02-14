#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

import requests

def number_of_subscribers(subreddit):
    """
    Function to return the number of subscribers.
    If invalid, function will return 0.
    """

    if not subreddit or not isinstance(subreddit, str):
        return 0

    headers = {'User-agent': 'Your Bot 1.0'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        results = response.json()
        return results.get('data', {}).get('subscribers', 0)
    except requests.RequestException as e:
        print(f"Error fetching subreddit data: {e}")
        return 0

# # Example usage
# subreddit_name = "python"
# subscribers = number_of_subscribers(subreddit_name)
# print(f"The number of subscribers in r/{subreddit_name}: {subscribers}")
