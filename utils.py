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
    randomListOfSymbols = [
        randint(33, 47),
        randint(58, 64),
        randint(91, 96),
        randint(123, 125),
    ]

    randomIndex = choice(randomListOfSymbols)

    return chr(randomIndex)
