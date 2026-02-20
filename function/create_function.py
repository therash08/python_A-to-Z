def is_even (num):
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'
    
for i in range(1,11):
    x = is_even(i)
    print(x)