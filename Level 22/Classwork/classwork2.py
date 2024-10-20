def filtered_mult(listn):
    mult = 1
    for i in listn:
        if i > 0:
            mult *= i

    return mult


print(filtered_mult([1,2,3,4,5,-1,2,-3]))