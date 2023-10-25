#!/usr/bin/python3
"""
module 0-gather_data_from_an_API
Returns information about an employee's TODO list from a REST API
"""
import requests
import sys

if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    response = requests.get(url).json()
    employee_name = response.get('name')

    url = 'https://jsonplaceholder.typicode.com/todos'.format(employee_id)
    response = requests.get(url).json()
    tasks = [task for task in response if task.get('userId') == employee_id]
    tasks_done = [task for task in tasks if task.get('completed')]

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          len(tasks_done),
                                                          len(tasks)))
    for task in tasks_done:
        print("\t {}".format(task.get('title')))
