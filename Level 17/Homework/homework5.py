numbers = []

for i in range (50,100 + 1):
    numbers.append(i)

for i in numbers:
    if i % 2 == 0:
        print(str(i) + "-" + str(numbers.index(i)))