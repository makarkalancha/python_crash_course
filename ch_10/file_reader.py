file_path = 'Crash_course/ch_10/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

print(contents)