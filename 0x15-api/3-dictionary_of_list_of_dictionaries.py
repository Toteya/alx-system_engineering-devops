#!/usr/bin/python3
"""
module 1-export_to_CSV
Export data gathered from API to CSV
"""
import json
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url).json()
    users = response

    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url).json()
    tasks = response

    filename = "todo_all_employees.json"
    json_dict = {}
    for user in users:
        id = user.get('id')
        username = user.get('username')
        details = []
        for task in tasks:
            if task.get('userId') == id:
                task_details = {
                        'username': username,
                        'task': task.get('title'),
                        'completed': task.get('completed'),
                    }
                details.append(task_details)
        json_dict.update({id: details})
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(json_dict, file)
