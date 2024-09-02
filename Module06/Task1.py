import random

list = []

def dice_roll():
    roll = random.randint(1, 6)
    return roll

list.append(dice_roll())

for i in list:
    if i != 6:
        dice_roll()
        list.append(dice_roll())
    else:
        print(list)
        break