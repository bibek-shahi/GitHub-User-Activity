GitHub User Activity CLI

This is a simple command-line application built with Python. It allows the user to enter a GitHub username and fetch that user's recent public activity using the GitHub API.

Features
Accepts a GitHub username from the command line
Fetches recent public GitHub activity
Shows Push Events
Shows Pull Request Events
Shows Starred Repositories
Handles invalid usernames
Uses only Python built-in libraries
How to Run

Open the terminal in the project folder and run:

python main.py <username>

Example:

python main.py octocat

Example Output

Pushed to: user/project

opened a pull request in: user/project

Starred a repo: user/project

Technologies Used
Python
GitHub API
urllib
JSON
What I Learned

This project helped me learn how to use command-line arguments, work with APIs, read JSON data, use loops and conditions, and handle errors using try and except.
