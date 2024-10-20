m = int(input("give me a number: "))
n = int(input("give me another number: "))

if m>n:
    for i in range (n,m):
        print(i**3)
elif m<n:
    for i in range (m,n):
        print(i**3)
else:
    print("enter different numbers")