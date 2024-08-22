number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

def sum(number1, number2, number3):
    return number1 + number2 + number3

def multiplication(number1, number2, number3):
    return number1 * number2 * number3

def average(number1, number2, number3):
    return int((number1 + number2 + number3) / 3)

if __name__ == "__main__":
    print(sum(number1, number2, number3))
    print(multiplication(number1, number2, number3))
    print(average(number1, number2, number3))




