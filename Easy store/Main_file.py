# import OS module
import os

# Get the list of all files and directories
path = "D:\Immigration"
#dir_list = os.listdir(path)

for path, subdirs, files in os.walk(path):
    for name in files:
        print(name, ":q", os.path.join(path, name))

#print("Files and directories in '", path, "' :")

#print('\n'.join(map(str, dir_list)))
