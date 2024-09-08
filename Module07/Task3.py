lentoasemat = {}

while True:
    print("\nValitse toiminto:")
    print("1 - Syötä uusi lentoasema")
    print("2 - Hae lentoaseman tiedot")
    print("3 - Lopeta")

    valinta = input("Anna valintasi (1, 2 tai 3): ")

    if valinta == "1":
        icao_koodi = input("Anna lentoaseman ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao_koodi] = nimi
        print(f"Lentoasema {nimi} lisätty koodilla {icao_koodi}.")

    elif valinta == "2":
        icao_koodi = input("Anna haettavan lentoaseman ICAO-koodi: ").upper()
        if icao_koodi in lentoasemat:
            print(f"Lentoasema {icao_koodi}: {lentoasemat[icao_koodi]}")
        else:
            print(f"Lentoasemaa ICAO-koodilla {icao_koodi} ei löytynyt.")

    elif valinta == "3":
        print("Ohjelma lopetetaan.")
        break

    else:
        print("Virheellinen valinta, yritä uudelleen.")