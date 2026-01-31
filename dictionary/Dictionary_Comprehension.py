# sq = {x: x**2 for x in range(1, 6)}
# print(sq)

keys = ['a','b','c','d','e']
values = [1, 2, 3, 4, 5]  

d = {k:v for (k,v) in zip(keys, values)}  
print (d)