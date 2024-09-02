import random

sides = int(input("Enter the number of sides on the dice: "))

list = []

def dice_roll(sides):
    roll = random.randint(1, sides)
    return roll

list.append(dice_roll(sides))

for i in list:
    if i != sides:
        dice_roll(sides)
        list.append(dice_roll(sides))
    else:
        print(list)
        break