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
            "eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU4",
            "0cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOi",
            "J1c2VyIiwiZXhwIjoxNzEzMDA0NDA4LjQ3OTY3MiwiaWF0IjoxNzEyOTE4MDA4L",
            "jQ3OTY3MiwianRpIjoiTFFBQ0JVSHJhX1Vtbk95ZzF6Vk5vZE1SLTRkVlZnIiwi",
            "Y2lkIjoiZzlkRFpQWWlGcW1GS2R0MTljVm1KQSIsImxpZCI6InQyXzNod3UxYmt",
            "zIiwiYWlkIjoidDJfM2h3dTFia3MiLCJsY2EiOjE1NTM3ODQ2NTQ3MTYsInNjcC",
            "I6ImVKeUtWdEpTaWdVRUFBRF9fd056QVNjIiwicmNpZCI6ImpKRFBfSjRtWnB0b",
            "25SQm5mZmVqWlNqR2RORWRiemhmU2lTbV9qMnhTLWsiLCJmbG8iOjh9.TWqOpyy",
            "mkwgQX9CR89lo21rBb4SZmFJoSdTHuvXPQuARh6T4z5sd0fSl3WavxGo8R6f3Ws",
            "YMEUReBTUbt9UQbuC_5J8RP6LnpIlUomgZVCkc480QzeKjYE5jxn1z4Kr4YMGq9",
            "b2Cn08HoMI56oYSmVKrvrkLAVFudT_F5jY5ty0Ix3R-b3gnSioEuhDGdE5iiYj3",
            "Cl6gprJVjfVrBeaYkPOoHGM5cMnsoypgxnXxk7S2kttzWQZgR6n7kjQuUh5z-A8",
            "ovswdHsCbZDLNzaS_K8ebKwqTAx1WEmhE_b46ocSC7de4iLIxPLlvEoyv7PUugQ",
            "BExABA0h9PF9I0yGMbzQ"]
        )

    # url = "https://www.reddit.com/dev/api/r/{}/about".format(subreddit)
    # url = "https://oauth.reddit.com/api/v1/me".format(subreddit)
    url = "https://oauth.reddit.com/r/{}/about".format(subreddit)
    headers = {
            'User-Agent': random.choice(user_agents),
            'Authorization': 'bearer {}'.format(access_token)
    }
    response = requests.get(url, headers=headers)
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
