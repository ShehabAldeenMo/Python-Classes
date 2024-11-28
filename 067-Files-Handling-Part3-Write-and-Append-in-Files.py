# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------

# will create it, if it's unexisted
myFile = open("/home/shehabaldeen/Desktop/MyComputer/Elzero-Python\shehab.txt", "w")
myFile.write("Hello\n")
myFile.write("Third Line")

# r: will ignore \r \n and so on ....
myFile = open(r"/home/shehabaldeen/Desktop/MyComputer/Elzero-Python\shehabfun.txt", "w")
myFile.write("Elzero Web School\n" * 1000)

myList = ["Oasma\n", "Ahmed\n", "Sayed\n"]

myFile = open("/home/shehabaldeen/Desktop/MyComputer/Elzero-Python\shehab.txt", "w")
myFile.writelines(myList)

myFile = open("/home/shehabaldeen/Desktop/MyComputer/Elzero-Python\shehab.txt", "a")
myFile.write("Shehab")