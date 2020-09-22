z = [1, 2, 3, 4, 5]


def binary(a, low, high, x):
    if low > high:
        return -1
    mid = (low + high) // 2
    if a[mid] == x:
        return mid
    elif a[mid] > x:
        binary(a, low, mid - 1, x)
    else:
        binary(a, mid + 1, high, x)


print(binary(z, 0, len(z) - 1, 3))
