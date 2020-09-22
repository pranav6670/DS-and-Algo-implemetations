def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


a = str(fact(100))
count = 0
for i in a:
    if i == '0':
        count += 1

print(count)
