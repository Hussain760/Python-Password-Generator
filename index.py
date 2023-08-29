import utils
from random import choice


def generator(integer):
    listOfRandomChar = [
        utils.UpperCase(),
        utils.LowerCase(),
        utils.Numbers(),
        utils.Symbols(),
    ]

    listOfPassword = []
    for x in range(integer):
        listOfPassword.append(choice(listOfRandomChar))

    password = "".join(listOfPassword)

    return password


length = int(input("Please Enter the Length of the Password:\n"))
numberOfPasswords = int(input("How many passwords do you need:\n"))

for x in range(numberOfPasswords):
    print(generator(length))
