i=int(input("type 1 for mile-kilometer and type 2 for kilometer-mile "))

if i==1:
    m=float(input("give me a number to transport to kilometer "))
    m=m/1.6
    print(m)
elif i==2:
    k=float(input("give me a number to transport to mile "))
    k=k/1.6
    print(k)
else:
    print("wrong decision ")
   