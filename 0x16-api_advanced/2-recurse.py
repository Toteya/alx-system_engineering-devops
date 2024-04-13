#!/usr/bin/python3
"""
module: 2-recurse
"""
import json
import random
import requests

user_agents = [
        "Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail by Toteya",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/201 Firefox",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Tots_App"
    ]


def recurse(subreddit):
    """
    Returns a list containing the titles of all hot articles for a given
    subreddit.
    """

    access_token = "".join([
            "eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU4",
            "0cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOi",
            "J1c2VyIiwiZXhwIjoxNzEzMTAwMjI4LjgxNDQzNSwiaWF0IjoxNzEzMDEzODI4L",
            "jgxNDQzNSwianRpIjoiM3E2c2hxaEt1TkRkajBEcEtkQ0U0Y1pIakctNWRRIiwi",
            "Y2lkIjoiZzlkRFpQWWlGcW1GS2R0MTljVm1KQSIsImxpZCI6InQyXzNod3UxYmt",
            "zIiwiYWlkIjoidDJfM2h3dTFia3MiLCJsY2EiOjE1NTM3ODQ2NTQ3MTYsInNjcC",
            "I6ImVKeUtWdEpTaWdVRUFBRF9fd056QVNjIiwicmNpZCI6ImpKRFBfSjRtWnB0b",
            "25SQm5mZmVqWlNqR2RORWRiemhmU2lTbV9qMnhTLWsiLCJmbG8iOjN9.gwpnx9W",
            "p9K9bZOGS01xbzLPeMaYV3xPJUY6eOYpvbOuJQPZGgdSvBz3tWGwZ_y_ySM10xm",
            "k_B8TL8cw88UxipU5bkvVzb8mwFjq3-XNrmZJ6vqcRw-KMsu4GW9sojRrRxfSIT",
            "LUqUwr-wVlXffYLpF6z0QSduFS5_mLarsVN1QLovenUkqgnFJvZ_QSA3HX2nFrb",
            "5R-q-JmJTJYCAz9V2P2_A7bO0_-cuv4d7G09Fyc42_kLC36qPcxBaT-YVAdNkKJ",
            "sao0M5IXPJ9bZlRCEVx8ynPhpVntYlclXxmgu7Pzo8xLnmA65aNvHT0Ej8iijk3",
            "6zxGF_FBItoMRBdkKbXA"
        ])

    # url = "https://www.reddit.com/dev/api/r/{}/about".format(subreddit)
    # url = "https://oauth.reddit.com/api/v1/me".format(subreddit)
    url = "https://oauth.reddit.com/r/{}/hot".format(subreddit)
    headers = {
            'User-Agent': random.choice(user_agents),
            'Authorization': 'bearer {}'.format(access_token)
    }

    titles = []
    count = 0
    after = ""
    while after is not None:
        response = requests.get(
                url,
                headers=headers,
                params={"after": after, "count": count}
            )
        try:
            response_data = response.json()
        except Exception:
            return None

        data = response_data.get('data')
        posts = data.get('children')

        if not posts:
            return None

        for post in posts:
            title = post.get('data').get('title')
            titles.append(title)

        after = data.get('after')
        # print(len(titles))
        # print(after)
        # print()

    # print(response.text)
    # print(json.dumps(data, indent=4))
    return titles
