# my_dict = {'1': 'Geeks', '2': 'For', '3': 'Geeks'}
# my_dict.clear()
# print(my_dict)

# d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
# print(d.get('Name'))
# print(d.get('Gender'))

d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
print(list(d.items())[1][0])
print(list(d.items())[1][1])

d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
print(list(d.keys()))