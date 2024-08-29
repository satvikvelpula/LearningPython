list = []

while True:
    try:
        prompt = int(input("Enter a number (enter string to quit): "))
        list.append(prompt)
        for i in list:
            list.sort(reverse=True)
            list = list[:5]
    except ValueError:
        print(list)
        break
