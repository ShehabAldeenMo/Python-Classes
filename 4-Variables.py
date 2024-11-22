# ------------------------------------------
# ----------------- Variables --------------
# ------------------------------------------
# Syntex => [Variable Name] [Assignment Operator] [Value]
#
# Naming Rules:
# [1] Can Start With (a-z-A-Z) or underscore
# [2] You can't start with numbers or special characters 
# [3] can Include (0-9) or underscore
# [4] Can't include special characters
# [5] "Name" is not like "name" [case Sensitive]
# ------------------------------------------


_myVariable = " I will be greate, I love you Shehab."
print(_myVariable)

name = "Shehab"             # single word : normal
MyName = "Shehab"           # Two words   : camelcase 
my_name = " Shehab Aldeen"  # Two words   : snake_case

x = 10 
x = "Yarab"                 # It's ok


# Reserved Words in naming variables
help("keywords")

a,b,c = 1,2,3   # It's ok, should make (#of variables = #of values) 