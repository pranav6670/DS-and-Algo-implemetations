def printz(n):
    if n == 0:
        return
    printz(n-1)
    print(n)


printz(10)
