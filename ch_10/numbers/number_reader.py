import json

filename = 'Crash_course/ch_10/numbers/numbers.json'

with open(filename) as f:
    numbers = json.load(f)

print(numbers)