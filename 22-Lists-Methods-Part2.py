# -------------------
# -- Lists Methods --
# -------------------

# clear()
a = [1, 2, 3, 4]
a.clear()
print(a)

print('='*50)

# copy()
b = [1, 2, 3, 4]
c = b.copy()

print(b)  # Main List
print(c)  # Copied List

print('='*50)

b.append(5)

print(b)  # Main List
print(c)  # Copied List

# count()
d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1))

print('='*50)

# index()
e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
print(e.index("Ramy"))

print('='*50)

# insert() --> (index,"string") will insert string before index
f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(0, "Test")
f.insert(-1, "Test")

print(f)

print('='*50)

# pop()
g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(-3))