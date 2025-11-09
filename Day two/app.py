# age = 16;

# print(id(age))


# age = 'manish'
# num = 16

# print('nume : '+ str(num))



# take input form user and print


# user = input('Enter your name : ')

# print('Your name is  : ',user)

import math

diameter = int(input('Enter diameter ? '))

if(diameter != str):
    radius = diameter / 2
    print('---------')
    print('Diameter is : ',diameter)

    print('Area of circle : ',math.pi*(radius*radius))
    
    print('---------')
else:
    print('Kindly fill input as numric values like 1,2,3,')
