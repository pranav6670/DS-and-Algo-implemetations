a = [1, 2, 3, 4, 5]


def binary(z, x):
    low, high = 0, len(z) - 1
    while low <= high:
        mid = (low + high) // 2
        if z[mid] == x:
            return mid
        elif z[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return -1


print(binary(a, 5))

