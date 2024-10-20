i=int(input("your grade "))

if i>89 and i<100:
    print("A")
elif i>79 and i<90:
    print("B")
elif i>69 and i<80:
    print("C")
elif i>59 and i<70:
    print("D")
elif i<60:
    print("F")
else:
    print("invalid number")