# ---------------------------------------------------
# ------------ 11-Strings-Methods-P3.py -------------
# ---------------------------------------------------

# index(substring,start,End)
a = "I Love Python"
print(a.index("P"))         # index number 7
print(a.index("P",0,10))    # index number 7
#print(a.index("P",0,5))    # Error and stop code

# find(substring,start,end)
b = "I Love Python"
print(b.find("P"))        # index number 7
print(b.find("P",0,10))   # index number 7
print(b.find("P",0,5))    # return -1

# rjust(width,fill char) ljust(width,fill char)
c = "Shehab"
print(c.rjust(10))            # fill with spaces
print(c.rjust(10,"#"))        # index number 7

# splitlines()
e = """ First
Second
Third
"""

print(e.splitlines())

e = "First\nSecond\nThird"
print(e.splitlines())

# expandtabs()
g = "Hello\tWorld\tfrom\tshehab"
print(g.expandtabs(2))

# istitle() as for islower() , isspaces() , isidentifier() => ok to be variable name, isalpha() => is alphatic string, isalnum() => is alphaptic and number
one = "I Love Python And 3G"
Two = "I Love Python And 3g"
print(one.istitle())
print(Two.istitle())


