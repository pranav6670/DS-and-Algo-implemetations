a = [2, 3, 5, 6, 7]


def linear(z, x):
    for i in range(len(z)):
        if x == z[i]:
            return i

    return -1


print(linear(a, 7))
