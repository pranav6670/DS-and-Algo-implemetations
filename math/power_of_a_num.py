def power(a, n):
    """O(n) solution"""
    res = 1
    for i in range(n):
        res *= a
    print(res)


"""
power(x, n)  = if n is even: power(x, n//2) * power(x, n//2)
                else: power(x, n-1) * x
"""


def power_efficient(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        y = power_efficient(x, n / 2)
        return y * y
    else:
        return x * power_efficient(x, n - 1)


print(power_efficient(2, 10))
