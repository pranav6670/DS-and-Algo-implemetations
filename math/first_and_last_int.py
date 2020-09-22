def first_int(n):
    first = n
    while first >= 10:
        first //= 10

    return int(first)


print(first_int(219))


def last_int(n):
    return n % 10


print(last_int(219))
