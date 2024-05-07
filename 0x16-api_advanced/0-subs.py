#!/usr/bin/python3
"How many subs?"
from requests import get as GET
import sys


def number_of_subscribers(subreddit):
    "subreddit: name of subreddit"
    r = GET(
        f"http://reddit.com/r/{subreddit}/about.json",
        headers={'User-Agent': "alx"},
        # allow_redirects=False
        ).json()['data']
    if 'subscribers' in r:
        return r['subscribers']
    else:
        return 0


sys.stdout.write('OK')
sys.stdout.flush()
