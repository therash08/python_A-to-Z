#del
# L = [1,2,3,4,5,6]
# print(L)
# del L
# print(L)

# L = [1,2,3,4,5,6]
# del L[-1]
# print(L)

# del L[1:3]
# print(L)

#remove

# L = [1,2,3,4,5,6]
# L.remove(4)
# print(L)

#pop
# L = [1,2,3,4,5,6]
# L.pop()
# L.pop()
# print(L)

#clear

L = [1,2,3,4,5,6]
L.clear()
print(L)


a = [10, 20, 30, 40, 50]

a.remove(30)  
print("After remove(30):", a)

popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a) 

del a[0]  
print("After del a[0]:", a)