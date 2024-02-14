import praw

def number_of_subscribers(subreddit):
    # Initialize Reddit instance
    reddit = praw.Reddit(client_id='your_client_id',
                         client_secret='your_client_secret',
                         user_agent='your_user_agent')

    try:
        # Get subreddit info
        subreddit_info = reddit.subreddit(subreddit)
        # Return number of subscribers
        return subreddit_info.subscribers
    except Exception as e:
        print("Error:", e)
        return None

# Example usage
subreddit_name = "python"
subscribers = number_of_subscribers(subreddit_name)
if subscribers is not None:
    print(f"The number of subscribers in r/{subreddit_name}: {subscribers}")
else:
    print("Failed to fetch subscriber count.")
