talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

formula = (talents * 20 * 32 + pounds * 32 + lots) * 13.3

kilograms = formula // 1000
grams = formula % 1000
print(f"{kilograms} kilograms and{grams: .2f} grams")









