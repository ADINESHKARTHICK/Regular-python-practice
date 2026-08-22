username = input('Enter the user name: ')

if len(username) > 12:
    print('The user name length must be less than 12')

elif not username.find(" ") == -1:
    print("The user name can't contain any spaces:")

elif not username.isalpha():
    print("The username can't contain any numeric values")

else:
    print(f'Hi {username}')
