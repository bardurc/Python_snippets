# Necessary import
import os


# os.listdir() returns all filenames in the current working directory
# output is a list
for e in os.listdir():
    # os.path.isdir() returns True if e is a directory and False if it is not a directory
    if os.path.isdir(e):
        [DO SOMETHING]
    # os.path.isdir() returns True if e is a file and False if it is not a file
    elif os.path.isfile(e):
        [DO SOMETHING]
