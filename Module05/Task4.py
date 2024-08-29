cities = []

while True:
    prompt = str(input("Enter the names of five cities: "))
    cities.append(prompt)

    if len(prompt) == 0:
        break

    if len(cities) == 5:
        for city in cities:
            print(city)
        break