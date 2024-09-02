gallon = int(input("Enter the conversion: (g/l): "))

def conversion(gallon):
    litres = gallon * 3.785
    statement = print(f'{gallon} gallons is {litres:.2f} litres')
    return statement

conversion(gallon)