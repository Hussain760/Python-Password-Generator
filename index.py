from random import choices

def getPositiveInteger(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("PLEASE ENTER POSITIVE NUMBERS ONLY")
            continue
        if value <= 0:
            print("PLEASE ENTER POSITIVE NUMBERS ONLY")
            continue
        return value

length = getPositiveInteger("Please Enter the Length of the Password:\n")
numberOfPasswords = getPositiveInteger("How many passwords do you need:\n")

while True:
    needUppercase = input("Do You Need Capital Letters? [Y/Enter/N]\n").lower()
    needLowercase = input("Do You Need Lower Letters? [Y/Enter/N]\n").lower()
    needNumbers = input("Do You Need Numbers? [Y/Enter/N]\n").lower()
    needSymbols = input("Do You Need Symbols? [Y/Enter/N]\n").lower()

    if needUppercase == "n" and needLowercase == "n" and needNumbers == "n" and needSymbols == "n":
        print("You Must Choose At Least One Option")
        continue
    break

listOfRandomChar = [
        False if needUppercase == "n" else 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        False if needLowercase == "n" else 'abcdefghijklmnopqrstuvwxyz',
        False if needNumbers == "n" else '0123456789',
        False if needSymbols == "n" else '!“#$%&‘()*+,-./:;<=>?@[]^_`{|}~\\',
]

filterList = ''.join([item for item in listOfRandomChar if item is not False])

def generator(lengthOfPassword):
    return ''.join(choices(filterList, k=lengthOfPassword))

password = [f"{x + 1}: {generator(length)}\n" for x in range(numberOfPasswords)]
print("".join(password))