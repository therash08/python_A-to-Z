# def multiply(a,b):
#     return a*b

# print(multiply(3,4))

# def multiply(*args):
#     product = 1

#     for i in args:
#         product = product * i
#     print(args)
#     return product

# print(multiply(1,4,5,6,7,8))

def fun(*args):
    for arg in args:
        print(arg)

fun(1,2,3,4,5)