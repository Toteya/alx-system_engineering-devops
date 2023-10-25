#!/usr/bin/python3
"""
module 1-export_to_CSV
Export data gathered from API to CSV
"""
import csv
import requests
import sys


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    response = requests.get(url).json()
    user_name = response.get('username')

    url = 'https://jsonplaceholder.typicode.com/todos'.format(employee_id)
    response = requests.get(url).json()
    tasks = [task for task in response if task.get('userId') == employee_id]

    filename = "{}.csv".format(employee_id)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            user_id = task.get('userId')
            task_status = task.get('completed')
            task_title = task.get('title')
            row = [user_id, user_name, task_status, task_title]
            writer.writerow(row)
