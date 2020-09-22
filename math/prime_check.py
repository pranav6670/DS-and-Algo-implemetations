def check_prime(n):
    """O(sqrt(n))"""
    if n == 1 or n <= 0:
        return False

    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False

    return True


# print(check_prime(7))


# More optimized solution

def check_prime_optimized(n):
    if n == 0 or n <= 0:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(n ** 0.5)):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


print(check_prime_optimized(121))
