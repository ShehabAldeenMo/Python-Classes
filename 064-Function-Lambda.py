# ------------------------
# -- Function => lambda --
# -- Anonymous Function --
# ------------------------
# [1] It Has No Name
# [2] You Can Call It Inline Without Defining  so it use when we didn't need to allocate memory for this function
# [3] You Can Use It In Return Data From Another Function
# [4] Lambda Used For Simple Functions and Def Handle The Large Tasks
# [5] Lambda is One Single Expression not Block Of Code
# [6] Lambda Type is Function
# -------------------------------------------------------------------

def say_hello(name, age) : return f"Hello {name} your Age Is: {age}"

hello = lambda name, age : f"Hello {name} your Age Is: {age}"

print(say_hello("Ahmed", 36))
print(hello("Ahmed", 36))

print(say_hello.__name__) # will give you the actual name of this function
print(hello.__name__)     # didn't have function name because it's a lambda function

print(type(hello))