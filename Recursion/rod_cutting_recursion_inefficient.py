def rod_cut(n, a, b, c):
    if n == 0:
        return 0
    if n < 1:
        return -1

    res = max(rod_cut(n - a, a, b, c),
              rod_cut(n - b, a, b, c),
              rod_cut(n - c, a, b, c))

    if res == -1:
        return -1

    return res + 1


print(rod_cut(23, 11, 9, 12))
