import os

path = "/"
dir_list = os.listdir(path)

print("Files and dirctories in '", path, "' :")

print(dir_list)


dir_list = os.listdir()
path1 = os.path.curdir

print("Files and dirctories in '", path1, "' :")

print(dir_list)