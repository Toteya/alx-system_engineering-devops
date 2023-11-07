#!/usr/bin/python3
"""module 0-subs"""
import requests
import random
import os
import json

user_agents = [
    'Toteya',
    'Nyandi',
    'Wilbard',
    'YaMwandingi'
]


def number_of_subscribers(subreddit=None):
    """Returns the number of subscribers to the given subreddit
    """
    # token = os.getenv('TOKEN')
    token = ''.join(['eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjV',
                     'mcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSl',
                     'dUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNjk5NDYwNzY3LjQyNzc3N',
                     'CwiaWF0IjoxNjk5Mzc0MzY3LjQyNzc3NCwianRpIjoiRzFPb045NGlT',
                     'a3FtRXdtSFZoNHBRQU5Qc2lXSW1nIiwiY2lkIjoiZzlkRFpQWWlGcW1',
                     'GS2R0MTljVm1KQSIsImxpZCI6InQyXzNod3UxYmtzIiwiYWlkIjoidD',
                     'JfM2h3dTFia3MiLCJsY2EiOjE1NTM3ODQ2NTQ3MTYsInNjcCI6ImVKe',
                     'UtWaXBLVFV4UmlnVUVBQURfX3d2RUFwayIsInJjaWQiOiJhTTFJc0tS',
                     'c1dRYlNPWVg0Z0Z3ZElpdTdYQVFadUMzaVlIUlpvLWRpelVrIiwiZmx',
                     'vIjo4fQ.cqjtr7INTLJ8ehYmSTFLbmvhfDXVZ-h03Yy0PCq08Ag7sbY',
                     'JvEeZlY7c95LjU0fk5kuHHcDpzzc5ImWJN942rS7tqpiiI-6dvYTkMB',
                     'Mzg9yzUn-N4MvVaVgy_aXTjHoM1q_Nxqo_BolyBW_3xTHLZ0GL11ucF',
                     'nDqOF_nxl8Y2jfj3Idfh2bHpO9mkeBn8B_QY4WaQk2MuvpaqZYRAU97',
                     'chkHnmtd_FCj8t1oAes0MEB7aqh7RZ1KU14YGXOTeh1h6p40Uh6CKI_',
                     'RphG1HqZTxSJFiR4LtqG9cd7j_zMYoT__8Y84CBefrEXR8maLQgIp55',
                     'ElOxcnjWR19kAT5ydPaA'])
    url = 'https://oauth.reddit.com//r/{}/'.format(subreddit)
    headers = {
            'User-Agent': random.choice(user_agents),
            'Authorization': 'bearer {}'.format(token),
        }
    response = requests.get(url, headers=headers)
    try:
        json_data = response.json().get('data').get('children')[0]
        num_subscribers = json_data.get('data').get('subreddit_subscribers')
    except Exception:
        num_subscribers = 0
    return num_subscribers
