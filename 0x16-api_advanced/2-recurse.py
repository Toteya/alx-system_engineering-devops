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
            "eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40",
            "cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1",
            "c2VyIiwiZXhwIjoxNzE1MTcxMDg3LjAwMTc0OCwiaWF0IjoxNzE1MDg0Njg3LjAw",
            "MTc0OCwianRpIjoid29sMDZCd29NenRmREJrdlNweE9KblRBMktfaUtRIiwiY2lk",
            "IjoiZzlkRFpQWWlGcW1GS2R0MTljVm1KQSIsImxpZCI6InQyXzNod3UxYmtzIiwi",
            "YWlkIjoidDJfM2h3dTFia3MiLCJsY2EiOjE1NTM3ODQ2NTQ3MTYsInNjcCI6ImVK",
            "eUtWdEpTaWdVRUFBRF9fd056QVNjIiwicmNpZCI6ImpKRFBfSjRtWnB0b25SQm5m",
            "ZmVqWlNqR2RORWRiemhmU2lTbV9qMnhTLWsiLCJmbG8iOjN9.bCmed6ZfMX1D-P_",
            "tiP7XSZgNnVH7GwYlxuTwxnd67OBBWTksM0XqKjrbqJ_xnC-gDoZii6h6w6gkrzc",
            "ZE33hAxsMRUltl1ipTDBoqcv1VxfRstFQrlLhwZMEAyeBRvgQ1277JsPuymJxBpw",
            "byMjNKCARtaqoJSnXa8hPehjwhn1unnHq_BPPxFAinxh69R7fn0H187D4qGbYr2z",
            "9890k4dzY3hhYFOD0pg4OvTGNkJKkpWROoCsaLAtJkj78y9MQJREF6053gq_jOD-",
            "8PMFGr7mSDMTXtLWqkTkyOhB0gf7l4_pyfnhpkfVmiNIneXw8exNKH_LcztewhyT",
            "XAftUzA"]
        )

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
        count += 1

    return titles
