# n = int(input('Enter a Nob : '))

# for i in range(1,n+1):
#     print(i, end='')





# set = {9}

# set.add(int(10.0))
# print(set)



X = int(input('X is : '))
Y = int(input('Y is : '))
choice = input(f'What do you want to do with these? X: {X} Y: {Y}  => ')

result = 0

if choice == '+':
    result = X + Y
elif choice == '-':
    result = X - Y
elif choice == '*':
    result = X * Y
else:
    print("Invalid choice!")

print('result:', result)





