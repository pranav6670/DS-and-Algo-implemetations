def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


a = 9
b = 6

print(gcd(a, b), lcm(a, b))

