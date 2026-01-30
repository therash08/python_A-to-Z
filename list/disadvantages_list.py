#  Disadvantages of Python Lists

# - Slow
# - Risky usage
# - eats up more memory

a = [1,2,3]
b = a.copy()

print(a)
print(b)

a.append(4)
print(a)
print(b)

# lists are mutable