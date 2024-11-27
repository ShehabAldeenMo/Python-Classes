# ---------------------------------------------------
# ------------ 10-Strings-Methods-P2.py --------------
# ---------------------------------------------------

# split() rsplit()

a = " I love python and Cpp"
print(a.split())  # split by spaces

b = " I-love-python-and-Cpp" 
print(b.split("-"))  # split by "-"

c = " I-love-python-and-Cpp" 
print(c.split("-",2))  # split by "-" for 2 elements only

c = " I-love-python-and-Cpp" 
print(c.rsplit("-",2))  # right split by "-" for 2 elements only

# center()
e = "Shehab"
print(e.center(10))       # spaces 
print(e.center(10,"#"))   # hashes

# count()
f = "I love Python and Cpp but Cpp is fall love with me"
print(f.count("Cpp"))      # 2 words
print(f.count("Cpp",0,25)) # Only one word between 0:25

# swapcase ()
g = "i AM dEVELOPER"
print(g.swapcase())

# startswith() , endswith --> starts with , ends with.
i = "I Love Python"
print(i.startswith("I"))
print(i.startswith("i"))
print(i.startswith("S"))

print(i.startswith("i",7,12))