# -------------------------------
# ---- set methods part 2 ----
# -------------------------------

a = {1,2,3,4}
b = {1,2,3,"shehab","Mohammed"}

print(a)
print(a.difference(b))
print("=" * 40) # separator

# difference_update()

c = {1,2,3,4}
d = {1,2,3,"shehab","Mohammed"}

print(c)
c.difference_update(d)
print(c)
print("=" * 40) # separator

# intersection
e = {1,2,3,4,5,6,8,9,"X"}
f = {"Shehab",8,9,"X"}
print(e)
print(e.intersection(f))
print("=" * 40) # separator

# intersection_update()

j = {1,2,3,4}
k = {"Abdallah",2,3,"shehab","Mohammed"}

print(j)
j.intersection_update(k)
print(j)
print("=" * 40) # separator

# symmetric_difference()

i = {1,2,3,4}
w = {"Abdallah",2,3,"shehab","Mohammed"}

print(i)
print(i.symmetric_difference(w))
print(i)
print("=" * 40) # separator


# symmetric_difference_update()

i = {1,2,3,4}
w = {"Abdallah",2,3,"shehab","Mohammed"}

print(i)
i.symmetric_difference_update(w)
print(i)
print("=" * 40) # separator