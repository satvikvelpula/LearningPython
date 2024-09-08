nimet = []

while True:
    nimi = input("Anna nimi (tai paina Enter lopettaaksesi): ")

    if nimi == "":
        break

    if nimi in nimet:
        print("Aiemmin syötetty nimi.")
    else:
        print("Uusi nimi.")
        nimet.append(nimi)

print("\nSyötetyt nimet:")
for nimi in nimet:
    print(nimi)