# ------------------------
# -- Built In Functions --
# ------------------------
# sum()   => summation between numbers 
# round() => nearly float number to int
# range() => will print range from begining to end
# print() => print 
# ------------------------

# sum(iterable, start)
a = [1, 10, 19, 40]
print(sum(a))
print(sum(a, 40))

# round(number, numofdigits)
print(round(150.501))
print(round(150.554, 2))

# range(start, end, step)
print(list(range(0)))
print(list(range(10)))
print(list(range(0, 20, 2)))

# print(), set | in separation spaces
print("Hello @ Osama @ How @ Are @ You")
print("Hello", "Osama", "How", "Are", "You", sep=" | ") # save your time to make it in each position

# end=" " in last position rather than \n
print("First Line", end=" ")
print("Second Line")
print("Third Line")