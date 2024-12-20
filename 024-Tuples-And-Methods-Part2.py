# -----------
# -- Tuple --
# -----------

# how to define Tuple With One Element ?

myTuple1 = ("Osama",)
myTuple2 = "Osama",

print(myTuple1)
print(myTuple2)

print('='*50)

print(type(myTuple1))
print(type(myTuple2))

print('='*50)

print(len(myTuple1))
print(len(myTuple2))

print('='*50)

# Tuple Concatenation
a = (1, 2, 3, 4)
b = (5, 6)

c = a + b
d = a + ("A", "B", True) + b

print(c)
print(d)

print('='*50)

# Tuple, List, String Repeat (*)
myString = "Osama"
myList = [1, 2]
myTuple = ("A", "B")

print(myString * 6)
print(myList * 6)
print(myTuple * 6)

print('='*50)

# Methods => count()
a = (1, 3, 7, 8, 2, 6, 5, 8)
print(a.count(8))

print('='*50)

# Methods => index()

b = (1, 3, 7, 8, 2, 6, 5)
# print("The Position of Index Is: " + b.index(7))  # Error in adding int with strings
print("The Position of Index Is: {:d}".format(b.index(7)))
print(f"The Position of Index Is: {b.index(7)}")

# Tuple Destruct
a = ("A", "B", 4, "C")

x, y, _, z = a

print(x)
print(y)
print(z)