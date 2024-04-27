#!/usr/bin/python3
"""Displays the user id using GitHub API and Basic Authentication."""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    # GitHub API endpoint for user information
    url = 'https://api.github.com/user'

    # Sending GET request with Basic Authentication
    response = requests.get(url, auth=(username, password))

    # Check if request was successful
    if response.status_code == 200:
        # Print the user id
        print(response.json()['id'])
    else:
        print("Failed to fetch user information. Status code:", response.status_code)

