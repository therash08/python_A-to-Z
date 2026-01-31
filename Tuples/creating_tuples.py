# t1 = ()
# print(t1)

# # create a tuple with a single item
# t2 = (2,)
# print(t2)
# print(type(t2))
# t2 = (2)
# print(t2)
# print(type(t2))


# # homo
# t3 = (1,2,3,4)
# print(t3)
# # hetro
# t4 = (1,2.5,True,[1,2,3])
# print(t4)

# # tuple
# t5 = (1,2,3,(4,5))
# print(t5)
# # using type conversion
# t6 = tuple('hello')
# print(t6)

# tup = ()
# print(tup)

# # Using String
# tup = ('Geeks', 'For')
# print(tup)

# # Using List
# li = [1, 2, 4, 5, 6]
# print(tuple(li))

# # Using Built-in Function
# tup = tuple('Geeks')
# print(tup)

tup = (5, 'Welcome', 7, 'Geeks')
print(tup)

# Creating a Tuple with nested tuples
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')
tup3 = (tup1, tup2)
print(tup3)

# Creating a Tuple with repetition
tup1 = ('Geeks',) * 3
print(tup1)

# Creating a Tuple with the use of loop
tup = ('Geeks')
n = 5
for i in range(int(n)):
    tup = (tup,)
    print(tup)