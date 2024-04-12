#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


def get_employee_name(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = f"{base_url}/{employee_id}"

    response = requests.get(url)
    return response.json().get('name')


def get_employee_tasks(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = f"{base_url}/{employee_id}/todos"

    response = requests.get(todo_url)
    tasks = response.json()
    return tasks


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide an employee ID as a command line argument.")
        sys.exit(1)

    employee_id = sys.argv[1]

    employee_name = get_employee_name(employee_id)
    tasks = get_employee_tasks(employee_id)

    done_tasks = [task for task in tasks if task.get('completed')]
    done = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks ({done}/{len(tasks)}):")

    for task in done_tasks:
        print(f"\t{task.get('title')}")
