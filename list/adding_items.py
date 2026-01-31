#append
# L = [1,2,3,4,5,6]
# L.append(100)
# L.append(200)
# L.append([1000,2000])
# print(L)

#extend
# L = [1,2,3,4,5,6]
# # L.extend([100,200,300])
# L.extend('dhaka')
# print(L)


#insert
# L = [1,2,3,4,5,6]
# L.insert(3,100)
# print(L)

a = [2,3,4,5,6]
a.append(8)
print(a)

a = [1, 2, 3]

a.append([4, 5])
print(a)

a = []
for i in range(5):
    a.append(i)
print(a)


a = [1, 2, 3]
b = [4, 5]

# Using extend() to add elements of b to a
a.extend(b)

print(a)


# Using a tuple
a = [1, 2, 3]
b = (4, 5)
a.extend(b)
print(a) 

# Using a set
a = [1, 2, 3]
b = {4, 5}
a.extend(b)
print(a)  

# Using a string
a = ['a', 'b']
b = "cd"
a.extend(b)
print(a)