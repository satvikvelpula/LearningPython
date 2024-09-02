import math

diameter = float(input("Enter the diameter of the first pizza in cm: "))
price = int(input("Enter the price of the first pizza in EUR: "))

diameter2 = float(input("Enter the diameter of the second pizza in cm: "))
price2 = float(input("Enter the price of the second pizza in EUR: "))

def unitpizza(diameter, price):
    cmtom = diameter / 100
    area = math.pi * (cmtom / 2)**2
    unitprice = area/price
    return unitprice

# print(f'First pizza unit price: {unitpizza(diameter, price)}')
# print(f'Second pizza unit price: {unitpizza(diameter2, price2)}')

if unitpizza(diameter, price) == unitpizza(diameter2, price2):
    print("Both of the pizzas provide the same money value. ")

elif unitpizza(diameter, price) > unitpizza(diameter2, price2):
    print("The first pizza unit price provides more value than the second pizza unit price. ")

elif unitpizza(diameter, price) < unitpizza(diameter2, price2):
    print("The second pizza unit price provides more value than the first pizza unit price. ")

