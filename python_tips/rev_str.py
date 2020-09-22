name = "Pranav"
reversed_str = ""
length = len(name)

for i in range(len(name), 0, -1):
    reversed_str += name[i-1]

print(reversed_str)


