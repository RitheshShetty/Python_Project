# import OS module
import os
import re

# Get the list of all files and directories
path = "D:\Immigration"
#dir_list = os.listdir(path)

for path, subdirs, files in os.walk(path):
    for name in files:
        names = re.split("_-", str(name))
        print(names)

#print("Files and directories in '", path, "' :")

#print('\n'.join(map(str, dir_list)))
