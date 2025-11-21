#lopp

# num = 1
# while num<=50:
#     if num %2 == 0:
#         print('Even => ',num)
#     else:
#         print('Odd : ',num)
#     num+=1      



# userInput = int(input('Enter num 1 to  n : '))
# num = 0
# sumOfuserInput = 0

# while num <= userInput:
#     sumOfuserInput+=num
#     num+=1

# print(f'addtion of num : {sumOfuserInput} ')


# write a programme lopp that print pattern loop 

# *
# **
# ***
# ****
# *****


# num = 0


# while num <= 5:
#     print('* ' * num)

#     num+=1


# userInput = 5
# num = 1

# while num <= 10:
#     print(f'5 *  {num}  : {num*userInput} ')

#     num+=1


 Print numbers from 1 to 100 using a for loop.

for num in range(1,101):
    print(num)

Print numbers from 100 to 1 using a while loop.

num = 100

while num >=1:
    print(num)

    num -= 1

Print all numbers between 1 and 50 except multiples of 5.

for i in range(5,51):
    if i % 5 == 0:
        print(i)

Create a program that asks the user for 5 favorite foods and prints them one by one.

num = 1

while num <= 5:
    userInput = input('Enter  favorite food  item : ')
    print( f'Food item  : {userInput}')
    num+=1

Print the sum of first 10 natural numbers using a while loop.
num = 0
add =0

while num <= 10:
    add = add + num
    num+=1

print(add)

