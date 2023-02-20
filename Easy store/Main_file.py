# import OS module
import os

# Get the list of all files and directories
path = "C://Users//Rithesh//Desktop"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# prints all files
print(dir_list)