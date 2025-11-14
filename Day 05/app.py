# language = []

# for count in range(1,3):
#     user = input(f'Enter {count} favorite language name: ')
#     language.append(user)

# print('Coding languages:', language)


heros = []

for count in range(3):
    userChoice = input('Enter your favorite actor of actress name here : - ')
    heros.append(userChoice)

print('Your heros List : ',heros)


tupple = (87, 64, 33, 95, 76) 


print(f'Tupple : {tupple}')

print(f'max num of tupple : {max(tupple)}')

print(f'min num of tupple : {min(tupple)}')



userMarks = int(input('Enter Your Obtained Marks : '))

if 80 <= userMarks <= 100:
    print('Student Grade : A')
elif 60 <= userMarks <= 70:
    print('Student Grade : B')
elif 45 <= userMarks <= 50:
    print('Student Grade : C')
else:
    print('Student Grade : F')



