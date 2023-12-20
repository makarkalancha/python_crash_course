import json

filename = 'Crash_course/ch_10/username/username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")