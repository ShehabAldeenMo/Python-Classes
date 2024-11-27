# ---------------------------------------------------
# ------------ 9-Strings-Methods-P1.py --------------
# ---------------------------------------------------
# I stoped at video 13


# length
a = "I Love python"
print(len(a))

# strip() rstrip() lstrip()
a = "           I Love python         "
print(a.strip())
print(a.rstrip()) # right
print(a.lstrip()) # left


a = "############I Love python #######"
print(a.strip('#'))
print(a.rstrip('#'))
print(a.lstrip('#'))

# title() => to make the first charachetr from each word is capital. And characters after numbers will be capital
b = "I love automotie cybersecurity, embedded baremetal, embedded linux, python"
print(b.title())

# capitalize() => to make the first charachetr from each word is capital. But characters after numbers willn't be capital
b = "I love automotie cybersecurity, embedded baremetal, embedded linux, python"
print(b.capitalize())

#zfil => zero fill to make numbers aligned
c,d,e,f = "1","11","111","1111"
print(c.zfill(3))
print(d.zfill(3))
print(e.zfill(3))
print(f.zfill(3))

# upper()
g = "shehab"
print(g.upper())

g = "SHEHAB"
print(g.lower())
