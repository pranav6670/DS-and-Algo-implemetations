def printz(n):
    if n == 0:
        return
    print(n)
    printz(n-1)


print(printz(10))
