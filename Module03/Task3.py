gender = str(input("What is your biological gender? (M/F): "))
hemoglobin = int(input("What is your hemoglobin value?: "))


if gender == "M":
    if hemoglobin > 167:
        print("Your hemoglobin is too high. ")
    elif hemoglobin < 134:
        print("Your hemoglobin is too low. ")
    else: print("Your hemoglobin is good. ")

elif gender == "F":
    if hemoglobin > 155:
        print("Your hemoglobin is too high. ")
    elif hemoglobin < 117:
        print("Your hemoglobin is too low. ")
    else: print("Your hemoglobin is good. ")
