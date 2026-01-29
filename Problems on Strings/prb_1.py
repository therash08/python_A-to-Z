# Find the length of a given string without using the len() function

s =input('enter a string: ')

counter = 0
for i in s:
    counter = counter + 1

print("length of string is", counter)