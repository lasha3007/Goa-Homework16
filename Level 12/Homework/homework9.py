m = int(input("give me a number: "))
n = int(input("give me another number: "))

d = int(input("type 1 for + , type 2 for - , type 3 for / , type 4 for * : "))

if d==1:
    print(m+n)
elif d==2:
    print(m+n)
elif d==3:
    print(m/n)
elif d==4:
    print(m*n)
else:
    print("wrong selection")