required_height=170
required_weight=50

height=int(input("your height "))
weight=int(input("your weight "))

if height >= required_height:
    print("you pass")
else:
    print("you are short")

if weight <= required_weight:
    print("you pass")
else:
    print("you are owerweight")