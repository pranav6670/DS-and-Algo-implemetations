def sumz(n):
    if n == 0:
        return 0
    else:
        return n + sumz(n-1)


print(sumz(5))