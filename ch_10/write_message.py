from datetime import datetime

filename = 'Crash_course/ch_10/programming.txt'
now = datetime.now()

with open(filename, 'w') as file_object:
    file_object.write(f"I love programming {now}")