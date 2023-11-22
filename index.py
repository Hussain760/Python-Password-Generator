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

needUppercase = input("Do You Need Capital Letters? [Y/Enter/N]\n").upper()
needLowercase = input("Do You Need Lower Letters? [Y/Enter/N]\n").upper()
needNumbers = input("Do You Need Numbers? [Y/Enter/N]\n").upper()
needSymbols = input("Do You Need Symbols? [Y/Enter/N]\n").upper()


def generator(integer):
    listOfPassword = []

    for x in range(integer):
        listOfRandomChar = [
            utils.UpperCase(),
            utils.LowerCase(),
            utils.Numbers(),
            utils.Symbols(),
        ]

        if needUppercase == "N":
            listOfRandomChar[0] = False

        if needLowercase == "N":
            listOfRandomChar[1] = False

        if needNumbers == "N":
            listOfRandomChar[2] = False

        if needSymbols == "N":
            listOfRandomChar[3] = False

        filterList = list(filter(lambda items: not (items == False), listOfRandomChar))

        listOfPassword.append(choice(filterList))

    password = "".join(listOfPassword)

    return password


for x in range(numberOfPasswords):
    print(f"{x + 1}: {generator(length)}\n")
