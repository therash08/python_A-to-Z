# def display(**kwargs):
#     for (key,value) in kwargs.items():
#         print(key, '->', value)
# print(display(india='delhi',srilanka='colombo',nepal='kathmandu',pakistan='islamabad'))

# L = [1,2,3,4]
# print(L.append(10))
# print(L)

def fun(**kwargs):
    for k,val in kwargs.items():
        print(f"{k}: {val}")

fun(name = 'rash', age = 23, city = 'sylhet')