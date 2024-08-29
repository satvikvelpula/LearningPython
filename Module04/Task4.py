import random

r = random.randint(1, 10)

while r > 0:
    guess = int(input("Guess the number between 1 and 10: "))
    if guess > r:
        print("Too high!")
    elif guess < r:
        print("Too low!")
    else:
        print("Correct!")
        break