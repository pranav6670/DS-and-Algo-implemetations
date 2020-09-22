from typing import *


def pal_check(string: str, start: int, end: int) -> bool:
    if start >= end:
        return True

    return string[start] == string[end] and pal_check(string, start=start + 1, end=end - 1)


a = "ABBA"
print(pal_check(a, 0, len(a) - 1))
