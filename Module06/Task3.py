def conversion(gallon):
    litres = gallon * 3.785
    return litres

while True:
    gallon = float(input("Enter the conversion: (g/l): "))
    if gallon <= 0:
        break
    else:
        print(conversion(gallon))