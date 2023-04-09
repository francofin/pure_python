import csv

user_password = input('please enter a password')

result = []

if len(user_password) >=8:
    result.append(True)
else:
    result.append(False)


digit = False
upperCase = False
for i in user_password:
    if i.isdigit():
        digit = True

result.append(digit)
for i in user_password:
    if i.isupper():
        upperCase = True

result.append(upperCase)
print(result)



if all(result):
    print("Strong Password")
else:
    print("Weak Password Provided")