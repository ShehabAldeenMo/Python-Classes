# -----------------
# -- Set Methods --
# -----------------

# issuperset()
a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}

print(a.issuperset(b))  # True, a contain b
print(a.issuperset(c))  # False, a not contain c

print("=" * 50)

# issubset()
d = {1, 2, 3, 4}
e = {1, 2, 3}
f = {1, 2, 3, 4, 5}

print(d.issubset(e))  # False, e not contain d
print(d.issubset(f))  # True, f contain d

print("=" * 50)

# isdisjoint()
g = {1, 2, 3, 4}
h = {1, 2, 3}
i = {10, 11, 12}

print(g.isdisjoint(h))  # False g intersect with h
print(g.isdisjoint(i))  # True g disintersect with h