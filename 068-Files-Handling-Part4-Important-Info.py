# -------------------------------------
# -- File Handling => Important Info --
# -------------------------------------

import os

myFile = open("/home/shehabaldeen/Desktop/MyComputer/Elzero-Python\shehab.txt", "a")
myFile.truncate(5)

# tell => the position of the cursor npw in your file
myFile = open("/home/shehabaldeen/Desktop/MyComputer/Elzero-Python\shehab.txt", "a")
print(myFile.tell())

# seek to stop on specofoc line
myFile = open("/home/shehabaldeen/Desktop/MyComputer/Elzero-Python\shehab.txt", "r")
myFile.seek(11)
print(myFile.read())

os.remove("/home/shehabaldeen/Desktop/MyComputer/Elzero-Python\shehab.txt")