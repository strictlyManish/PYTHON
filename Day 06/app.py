# obj = {
#     "name" : "mmanish Kumar",
#     "Class " : "Graduation"
# }

# for keys in obj:
#     print(keys ,' :  ' ,obj[keys])


# 1  Create a dictionary storing meanings of 3 English words.

word_meaning = {

    "Serene" : "Calm, peaceful, and untroubled",
    "Versatile" : "Able to adapt or be used for many different purposes",
    "Illuminate" : "To light up or make something clearer or easier to understand"
}

# print(word_meaning)

# 2  Create a set of numbers and show union and intersection with another set.

setA = {1, 2, 3}
setB = {3, 4, 5}



print(f'Union of {setA} and {setB} :  ', setA.union(setB))
print(f'Intersection of {setA} and {setB} :  ', setA.intersection(setB))

# 3  Try to add both integer 9 and float 9.0 to a set and observe what happens.

myset = {9}

myset.add(9.0)

print(myset) #  Output will be  {9} , cause 9 and 9.0 hava diffrend types but both are number

myset.add('9.0')

print(myset) #  Output will be  {9 , 9.0}  cause 9 is num and 9.0 is string 
