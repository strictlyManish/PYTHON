userExpencess = []

print('Welcome to Expence Tracker | 🤑')


while True:
    print('---------- [ MENU ] ------------')
    print('1. Add Expencess -- ')
    print('2. View all Expencess --  ')
    print('3. Grand Total Of Expencess : -- ')
    print('4. Exit to this menu ❌')

    userChoice = int(input('Enter Your Choice In Given Options '))

    if userChoice == 1:
        # Add all expencess ==
        userDate = input('Day of Splash Out : ')
        userCat = input('Category : Food , Travel etc. : ')
        userDisc = input('Enter Short Discription : ')
        userAmount = float(input('Enter Total amount : '))

        expence = {
            "date": userDate,
            "Expence Category": userCat,
            "Expence Discription": userDisc,
            "Total": userAmount
        }
        userExpencess.append(expence)
        print('Expencess Added Sucessfully')

    elif userChoice == 2:
        # View all expencess ==
        if len(userExpencess) == 0:
            print('Try to do some shoping.')
        else:
            for i in userExpencess:
                print(i)

    elif userChoice == 3:
        # Grand total ==
        total = 0
        for exp in userExpencess:
            total += exp['Total']
        print("Grand Total :", total)

    elif userChoice == 4:
        print('You are sucessfully Exits Your tracker')
        break

    else:
        print('Wrong Input Entered 📝')
