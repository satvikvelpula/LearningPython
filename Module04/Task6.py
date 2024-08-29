import random

while True:
    try:
        N = int(input("Enter the total amount of points to generate (enter string to quit): "))
        n = 0
        for i in range(N):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            if x ** 2 + y ** 2 <= 1:
                n += 1
        pi = 4 * n / N
        print(f'The approximate value of pi is {pi}')
    except ValueError:
        break