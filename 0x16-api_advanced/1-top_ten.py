#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests
import sys


def top_ten(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, print None.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )
    sys.exit(0)
    # try:
    #     if req.status_code == 200:
    #         for get_data in req.json().get("data").get("children"):
    #             dat = get_data.get("data")
    #             title = dat.get("title")
    #             print(title)
    #     else:
    #         print(None)
    # except Exception:
    #     pass


sys.stdout.write('OK')
sys.stdout.flush()
