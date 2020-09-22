a = 2525


def add(n):
    if n < 10:
        return n

    return add(n//10) + n % 10


def addz(n):
    n = str(n)
    a = 0
    for i in range(len(n)):
        a += int(n[i])
    return a



