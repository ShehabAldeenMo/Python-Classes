# ---------------------------
# -- Dictionary --
# ----------------
# [1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Element With Key
# ----------------------------

# Dictionary --> Key (immutable) : Value (any type of values)

user = {
  "name": "Osama",
  "age": 36,
  "country": "Egypt",
  "skills": ["Html", "Css", "JS"],
  "rating": 10.5
}

print(user)
print(user.get("country"))
print(user.keys())
print(user.values())

languages = {
    "One": {
        "name": "Html",
        "Progress" : "80%"
    },
    "Two": {
        "name": "Cpp",
        "Progress" : "60%"        
    },
    "Three": {
        "name": "Python",
        "Progress" : "90%"        
    }
}

print(languages['One'])
print(languages['One']['Progress'])
print(len(languages))
print(len(languages['One']))


# Create Dictionary From Variables

frameworkOne = {
  "name": "Vuejs",
  "progress": "80%"
}

frameworkTwo = {
  "name": "ReactJs",
  "progress": "80%"
}

frameworkThree = {
  "name": "Angular",
  "progress": "80%"
}

allFramework = {
  "one": frameworkOne,
  "two": frameworkTwo,
  "three": frameworkThree
}

print(allFramework)