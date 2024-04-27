#!/usr/bin/python3
"""Lists 10 most recent commits of a repository by a user using GitHub API."""

import sys
import requests

if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    params = {
        "per_page": 10,
        "page": 1
    }

    response = requests.get(url, params=params)
    commits = response.json()

    for commit in commits:
        sha = commit['sha']
        author = commit['commit']['author']['name']
        print(f"{sha}: {author}")

