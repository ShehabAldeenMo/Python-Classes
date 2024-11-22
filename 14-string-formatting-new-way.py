# ---------------------------------------------------
# -------- 13-string-formatting-new-way.py ----------
# ---------------------------------------------------

name = "Shehab"
age = 22
rank = 54

# {:s} => string
# {:d} => Number
# {:f} => float

print("My Name is: {}".format(name))
print("My Name is: {:s} and my age is: {:d}".format(name,age) )
print("My Name is: {:s} and my age is: {:f}".format(name,age) )
print("My Name is: {:s} and my age is: {:.2f}".format(name,age) )

# Truncate string
MyLongString = "Hello Peoples of Shehab Who is Embedded Developer"
print("Message is: {:.13s}".format(MyLongString) )

# format money
mymoney = 5045862001684
print("My money in bank: {:,d}".format(mymoney))

# Rearrange Items
a,b,c = "One","Two","Three"
print("Hello {1} {2} {0}".format(a,b,c))

a,b,c = 10,20,30
print("Hello {1} {2} {0}".format(a,b,c))

a,b,c = 10,20,30
print("Hello {1:d} {2:.5f} {0:d}".format(a,b,c))

# Format in version 3.6+
MyName = "shehab"
print("my name is {MyName}")
print(f"my name is {MyName}")