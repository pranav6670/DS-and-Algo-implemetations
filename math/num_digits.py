from math import *


def num_digits_iterative(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1

    return count


print(num_digits_iterative(1021113))


def num_digits_recursive(n):
    if n == 0:
        return 0
    return 1 + num_digits_recursive(n // 10)


print(num_digits_recursive(1021113))


def num_digits_log(n):
    return floor(log10(n) + 1)


print(num_digits_log(1021113))
