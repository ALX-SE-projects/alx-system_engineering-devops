from requests import get as GET


def number_of_subscribers(subreddit):
    r = GET(
        f"http://reddit.com/r/{subreddit}/about.json",
        headers={'User-Agent': "alx"},
        # allow_redirects=False
        ).json()['data']
    # r = r.json()
    # print(r)
    if 'subscribers' in r:
        return r['subscribers']
    else:
        return 0
    # print(r.text)
