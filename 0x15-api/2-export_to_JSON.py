#!/usr/bin/python3
"""
module 1-export_to_CSV
Export data gathered from API to CSV
"""
import json
import requests
import sys


if __name__ == '__main__':
    user_id = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = requests.get(url).json()
    user_name = response.get('username')

    url = 'https://jsonplaceholder.typicode.com/todos'.format(user_id)
    response = requests.get(url).json()
    tasks = [task for task in response if task.get('userId') == user_id]

    filename = "{}.json".format(user_id)
    details = []
    json_dict = {user_id: details}
    for task in tasks:
        task_details = {
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': user_name
            }
        details.append(task_details)
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(json_dict, file)
