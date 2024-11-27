# ---------------------------
# -- Dictionary Methods --
# ---------------------------

# setdefault(key,value)
user = {
  "name": "Baba"
}
print(user)
print(user.setdefault("name", "shehab"))
print(user.setdefault("age", 36))
print(user)

print("=" * 40)

# popitem()

member = {
  "name": "Shehab",
  "skill": "PS4"
}
print(member)
member.update({"age": 36})
print(member)
print(member.popitem())

print("=" * 40)

# items()
view = {
  "name": "Osama",
  "skill": "XBox"
}

print("=" * 40)
print("=" * 40)

allItems = view.items()
print(allItems)
view["age"] = 36

print(allItems)

print("=" * 40)

# fromkeys()

a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')
b = ("X","Y")

print(dict.fromkeys(a, b))