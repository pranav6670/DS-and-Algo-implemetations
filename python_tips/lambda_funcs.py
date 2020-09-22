def sum_5(x):
    return x + 5


a = lambda i: i + 5

#######################


def sum2(x, y):
    return x + y


b = lambda x, y: x + y

print(b(1, 2))

#######################


x = [1, 2, 3, 4, 5]

pow_list = list(map(lambda z: z**2, x))
print(pow_list)
even_list = list(filter(lambda y: y % 2 == 0, x))
print(even_list)







