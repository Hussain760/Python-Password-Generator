import utils
from random import choice

while True:
    try:
        length = int(input("Please Enter the Length of the Password:\n"))
        if length <= 0:
            raise Exception()
        break
    except:
        print("PLEASE ENTER POSITIVE NUMBERS ONLY")

while True:
    try:
        numberOfPasswords = int(input("How many passwords do you need:\n"))
        if numberOfPasswords <= 0:
            raise Exception()
        break
    except:
        print("PLEASE ENTER POSITIVE NUMBERS ONLY")

needUppercase = input("Do You Need Capital Letters? [Y/Enter/N]\n").lower()
needLowercase = input("Do You Need Lower Letters? [Y/Enter/N]\n").lower()
needNumbers = input("Do You Need Numbers? [Y/Enter/N]\n").lower()
needSymbols = input("Do You Need Symbols? [Y/Enter/N]\n").lower()

def generator(integer):
    listOfPassword = []
    listOfRandomChar = [
            False if needUppercase == "n" else utils.UpperCase,
            False if needLowercase == "n" else utils.LowerCase,
            False if needNumbers == "n" else utils.Numbers,
            False if needSymbols == "n" else utils.Symbols,
    ]
    filterList = list(filter(lambda items: not (items == False), listOfRandomChar))

    for x in range(integer):
        listOfPassword.append(choice(filterList)())   # choice(filterList)() runs the functions (utils.UpperCase, utils.LowerCase, etc.)

    password = "".join(listOfPassword)

    return password


for x in range(numberOfPasswords):
    print(f"{x + 1}: {generator(length)}\n")
