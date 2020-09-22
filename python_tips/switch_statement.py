def switch(arg):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }

    return switcher.get(arg, "Nothing")


print(switch(5))