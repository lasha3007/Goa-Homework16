num = int(input("Enter number: "))
num2 = int(input("Enter number: "))
num3 = int(input("Enter number: "))
num4 = int(input("Enter number: "))
num5 = int(input("Enter number: "))
lists = []
lists.append(num)
lists.append(num2)
lists.append(num3)
lists.append(num4)
lists.append(num5)

num = 0

for i in lists:
    num += i
print(num)