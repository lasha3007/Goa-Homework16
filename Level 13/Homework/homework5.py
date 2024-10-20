guess_number = 7
while True:
    user = int(input("Guess the number beetween 1-10: "))
    if user == guess_number:
        print("You won <3")
        break
    else:
        print("You lost Try again!!!")