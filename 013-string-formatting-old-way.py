# ---------------------------------------------------
# -------- 13-string-formatting-old-way.py ----------
# ---------------------------------------------------

name = "Shehab"
age  = 22
rank = 54

print("My Name is: " + name)

# %s => string
# %d => Number
# %f => float

print("My Name is: %s" % name)
print("My Name is: %s and my age is: %d" % (name,age) )
print("My Name is: %s and my age is: %f" % (name,age) )
print("My Name is: %s and my age is: %.2f" % (name,age) )

# Truncate string
MyLongString = "Hello Peoples of Shehab Who is Embedded Developer"
print("Message is: %.5s" % MyLongString)