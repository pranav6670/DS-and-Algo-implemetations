def eratosthenes(n):
    is_prime = [True] * n
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(n**0.5)+1):
        for j in range(2*i, n, i):
            is_prime[j] = False

    return [x for x in range(n) if is_prime[x]], [x for x in range(n) if not is_prime[x]]


print("Primes are: ")
print(eratosthenes(1500)[0])

print("\nCo-primes are: ")
print(eratosthenes(1500)[1])
