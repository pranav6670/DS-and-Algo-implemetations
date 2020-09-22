def fun1(n):
    if n == 0:
        return
    print(n)
    fun1(n-1)
    print(n)


def fun2(n):
    if n == 0:
        return
    fun2(n-1)
    print(n)
    fun2(n-1)


fun2(3)
