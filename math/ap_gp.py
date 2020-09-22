def nth_term_AP(a, d, n):
    return a + (n - 1) * d


print(nth_term_AP(2, 2, 10))


def nth_term_GP(a, r, n):
    return a * r ** (n - 1)


print(nth_term_GP(2, 2, 10))


def sum_nterms_AP(a, d, n):
    return int(n / 2 * (2 * a + (n - 1) * d))


print(sum_nterms_AP(1, 1, 5))
