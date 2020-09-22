import math


def firstDigit(n):
    digits = int(math.log10(n))

    n = int(n / pow(10, digits))

    return n


def lastDigit(x):
    return x % 10


n = 12345
print(firstDigit(n), end=" ")
print(lastDigit(n))
