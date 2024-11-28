# --------------------
# -- Function Scope --
# --------------------

x = 1  # Global Scope

def one():
  
  # x = 10 # if we use it without Global keyword will lead to define it as local var

  global x # to overwrite on Global instance

  x = 2

  print(f"Print Variable From Function Scope {x}")

def two():

  x = 10 # local

  print(f"Print Variable From Function Scope {x}")

one()
print(f"Print Variable From Global Scope {x}")
two()
print(f"Print Variable From Global Scope After One Function Is Called {x}")