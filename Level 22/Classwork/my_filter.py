my_filter = [1,5, 10, 123, 55,1,1331]

print(my_filter)

n = int(input("which one whould you remove: "))

for  i in my_filter:
    if i == n:
        my_filter.remove(i)

print(my_filter)