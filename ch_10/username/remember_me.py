import json

username = input("What is your name? ")

filename = 'Crash_course/ch_10/username/username.json'

with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")