numbers = []

for i in range (10,50 + 1):
    if i%4==0:
        numbers.append(i)

numbers.reverse()

print(numbers)