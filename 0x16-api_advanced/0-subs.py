#!/usr/bin/python3
"""
module 0-subs
Returns the number of total subsbribers for a given subreddit
"""
import json
import random
import requests

user_agents = [
        "Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail by Toteya",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/201 Firefox",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Tots_App"
    ]


def number_of_subscribers(subreddit):
    """
    Returns the number of subscriber for the given subreddit
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

    # url = "https://www.reddit.com/dev/api/r/{}/about".format(subreddit)
    # url = "https://oauth.reddit.com/api/v1/me".format(subreddit)
    url = "https://oauth.reddit.com/r/{}/about".format(subreddit)
    headers = {
            'User-Agent': random.choice(user_agents),
            'Authorization': 'bearer {}'.format(access_token)
    }
    response = requests.get(url, headers=headers)

    if response.status_code >= 400:
        return 0

    try:
        response_data = response.json()
    except Exception:
        return 0

    # print(response.text)
    # print(json.dumps(response_data, indent=4))

    data = response_data.get('data')
    subs = data.get('subscribers')
    if subs is None:
        return 0
    return int(subs)
