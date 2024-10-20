def filtered_sum(listn):
    mult = 0
    for i in listn:
        if i % 2 != 0:
            mult += i

    return mult+5


print(filtered_sum([1,2,3,4,5,-1,2,-3]))