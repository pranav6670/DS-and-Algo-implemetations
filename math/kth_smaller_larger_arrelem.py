from typing import *


def k_small_large(arr: List, k: int, type_metric: str) -> int:
    if type_metric == "Smaller":
        arr.sort()
        return arr[k-1]
    elif type_metric == "Larger":
        arr.sort(reverse=True)
        return arr[k-1]


array = [1, 5, 4, 3, 2]


print(k_small_large(array, 2, "Larger"))
