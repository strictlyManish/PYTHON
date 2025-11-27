# Write a function to calculate the factorial of a number.


def factorial(n):
    fact = 1
    while n > 1:
        fact = fact * n
        n = n - 1
    return fact

# a = factorial(5)  ## 120

# Write a function that checks if a number is prime.

def isPrime(n):
    if n % 2 != 0:
        return 'Prime'
    else:
        return 'Not a Prime'


# print(isPrime(5))      


# Write a function greet_user(name) that prints a personalized message for you


def greet_user(name):
    print(f'Hey welcome {name}')

# greet_user('manish rajz')  


# Write a function to return the largest of 3 numbers.


def largestOf3():
    for i
  