def likes(names):
    xt = ""

    if (len(names) == 0):
        xt = "no one likes this"
    elif (len(names) == 1):
        xt = str(names[0]) + " likes this"
    elif (len(names) > 1 and len(names) < 4):
        for name in range(0, len(names) - 1):
            xt = xt + names[name] + ", "
        xt = xt[:-2]
        xt = xt + " and " + str(names[len(names) - 1]) + " like this"
    else:
        for name in range(0, 2):
            xt = xt + names[name] + ", "
        xt = xt[:-2]
        xt = xt + " and " + str(len(names)-2) + " others like this"
    return xt