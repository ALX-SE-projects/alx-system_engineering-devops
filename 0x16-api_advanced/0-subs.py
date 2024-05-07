#!/usr/bin/python3
"How many subs?"
from requests import get as GET


def number_of_subscribers(subreddit):
    "subreddit: name of subreddit"
    req = GET(
        f"http://reddit.com/r/{subreddit}/about.json",
        headers={'User-Agent': "alx"},
        # allow_redirects=False
        )
    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
