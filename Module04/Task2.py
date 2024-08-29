inches = 1

while inches > 0:
    inches = float(input("Enter inches: "))
    if inches < 0:
        break
    else:
        print(inches * 2.54)