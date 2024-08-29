n = []

while True:
    try:
        prompt = int(input("Enter a number: "))
        n.append(prompt)
    except ValueError:
        print(f'Largest number in list: {max(n)}')
        print(f'Smallest number in list: {min(n)}')
        break