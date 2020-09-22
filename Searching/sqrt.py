"""Naive approach"""


def square_root_naive(n):
    """O(sqrt(n))"""
    i = 1
    while i ** 2 <= n:
        i += 1

    return i - 1


print("Naive: ", square_root_naive(64))

"""Better Approach"""


def bin_search_sqrt(x):
    """O(log x)"""
    low, high = 0, x
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        mid_sq = mid ** 2
        if mid_sq == x:
            return mid
        elif mid_sq > x:
            high = mid - 1
        else:
            low = mid + 1
            ans = mid
    return ans


print("Optimized: ", bin_search_sqrt(64))
