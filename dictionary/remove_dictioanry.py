# d = {1: 'Geeks', 2: 'For', 3: 'Geeks', 'age':22}

# # Using del 
# del d["age"]
# print(d)

# d = {"small": "big", "black": "white", "up": "down"}
  
# # delete key-value pair with key "black" from my_dict1
# del d["black"]
  
# # check if the  key-value pair with key "black" from d1 is deleted
# print(d)


d = {'a': 1, 'b': 2, 'c': 3}
v = d.pop('b')
print(v)  

v = d.pop('d', 'Not Found')
print(v)