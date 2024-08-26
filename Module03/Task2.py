lux = "LUX: Upper-deck cabin with a balcony."
a = "Above the car deck, equipped with a window."
b = "Windowless cabin above the car deck."
c = "Windowless cabin below the car deck."

prompt = input("Enter the cabin class of a cruise ship (LUX, A, B, C): ")

if prompt == "LUX":
    print(lux)
elif prompt == "A":
    print(a)
elif prompt == "B":
    print(b)
elif prompt == "C":
    print(c)
else:
    print("Not a valid cabin class")

