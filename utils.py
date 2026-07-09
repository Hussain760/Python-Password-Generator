# Collecting All The Chractors From ASCII Table
# Check Out ASCII Char Table On https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html

from random import randint, choice


def UpperCase():
    randomIndex = randint(65, 90)
    return chr(randomIndex)


def LowerCase():
    randomIndex = randint(97, 122)
    return chr(randomIndex)


def Numbers():
    randomIndex = randint(48, 57)
    return chr(randomIndex)


def Symbols():
    randomListOfSymbols = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47,
                           58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 95, 96, 123, 124, 125]

    randomIndex = choice(randomListOfSymbols)

    return chr(randomIndex)
