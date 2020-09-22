a = [x for x in range(1, 10)]
b = [y for y in range(5, 15)]


def intersection(l1, l2):
    intersec_list = [z for z in l1 if z in l2]
    return intersec_list


def union(l1, l2):
    final_list = list(set(l1) | set(l2))
    return final_list


print(a, b, sep="\n")
print(intersection(a, b))  # print(list(filter(lambda x: x in a, b)))

print(union(a, b))
