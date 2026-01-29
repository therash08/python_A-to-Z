email = input('enter email')
Password = input('enter Pass')

if email == 'therash@gmail.com' and Password == '1234':

    print("welcome")
if email == 'therash@gmail.com' and Password != '1234':
    print('incorrect pass')
    Password = input('enter pass again')
    if Password == '1234':
        print("Welcome,finally!") 
    
else:
    print("try again brother")

