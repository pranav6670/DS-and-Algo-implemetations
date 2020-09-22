"""Naive approach"""


def square_root(n):
    """O(sqrt(n))"""
    i = 1
    while i * i <= n:
        i += 1

    return i - 1


print(square_root(81))

