import requests

USER_AGENT = {'User-agent': 'Mozilla/5.0'}  # Updated user-agent to a common browser


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    # Validating subreddit input
    if not isinstance(subreddit, str) or " " in subreddit or not subreddit.startswith("r/"):
        return None  # Invalid subreddit format

    url = f'https://www.reddit.com/{subreddit}/about.json'
    try:
        response = requests.get(url, headers=USER_AGENT)
        response.raise_for_status()  # Raises an exception for 4XX and 5XX status codes
        results = response.json()
        return results.get("data").get("subscribers")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


# Example usage
subreddit_name = "r/learnpython"
subscribers_count = number_of_subscribers(subreddit_name)
if subscribers_count is not None:
    print(f"The number of subscribers in {subreddit_name} is: {subscribers_count}")
else:
    print("Failed to retrieve subscriber count.")
