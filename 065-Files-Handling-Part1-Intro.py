# -------------------
# -- File Handling --
# -------------------
# "a" Append  Open File For Appending Values, Create File If Not Exists 
# "r" Read    [Default Value] Open File For Read and Give Error If File is Not Exists
# "w" Write   Open File For Writing, Create File If Not Exists
# "x" Create  Create File, Give Error If File Exists
# --------------------------------------------------

import os # will discuss next

# Main Current Working Directory
print(os.getcwd())

# Directory For The Opened File now in your code 
# will appear the files exists in your opened file directory
# __file__ : your current file
# os.path.abspath(__file__) : will get absolut path for your now file
# os.path.dirname : will return your directory name that the opened file exists in
print(os.path.dirname(os.path.abspath(__file__)))

print('='*50)

# Change Current Working Directory
# os.chdir : will change your current working directory to the opened file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(os.getcwd())

print(os.path.abspath(__file__))

print('='*50)

# r to neglect the existabce of any  escape sequence characters as \n \r and so on ... 
# default action is read and will give error if this file isn't exist
file = open(r"D:\Python\Files\nfiles\shehab.txt")

file = open("D:\Python\Files\osama.txt")