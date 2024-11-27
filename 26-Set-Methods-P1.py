# --------------------------
# ---- set methods ----
# --------------------------

# clear()
a = {1,2,3,4,5,6,7}
a.clear()
print(a)

print('='*50)

# union()
b = {"One","Two","Three"}
c = {"1","2","3"}
x = {"Zero","Cool"}

print(b | c)
print (b.union(c,x))

# add()
d = {1,2,3,4,5}
d.add(6)
d.add(7)
print(d)

e = {1,2,3,4,5,6}
f = e.copy()

print(e)
print(f)

e.add(7)
print(e)


# remove ()
g = {1,2,3,4,5,6}
g.remove(1)
# g.remove(8)     # Will give yoy error 
print(g)

print('='*50)

# discard ()
h = {1,2,3,4,5,6}
h.discard(1)
h.discard(8)     # Willn't give yoy error 
print(h)


# pop()
i = {"A",True,1,2,3,4,5,6}
print(i.pop())

print('='*50)

# update ()
j = {1,2,3,4,5,6,7,8,9}
k = {1,"A","B","C",2}

j.update(k)
print(j)

