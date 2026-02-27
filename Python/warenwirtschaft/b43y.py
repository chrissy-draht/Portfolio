# b43.py
# Modul: Eingabeprüfungen

def eingabe_artikelnummer(artikel_liste):
    """
    Fragt eine Artikelnummer ab.
    Erlaubt: 0 zum Beenden oder eine vorhandene Artikelnummer aus 'artikel_liste'.
    artikel_liste: Dict {artikelnummer: (name, preis)}
    Gibt int zurück.
    """
    erlaubte = ", ".join(str(nr) for nr in artikel_liste.keys())

    while True:
        text = input("Artikelnummer (0 = Ende): ").strip()

        try:
            artikelnummer = int(text)
        except ValueError:
            print("Eingabefehler: Bitte eine ganze Zahl eingeben. Erlaubt: " + erlaubte + " oder 0.")
            continue

        if artikelnummer == 0:
            return 0

        if artikelnummer in artikel_liste:
            return artikelnummer

        print("Unbekannte Artikelnummer! Erlaubt sind: " + erlaubte + " oder 0.")


def eingabe_menge():
    """
    Fragt die Menge ab.
    Erlaubt: ganze Zahl > 0.
    Gibt int zurück.
    """
    while True:
        text = input("Menge: ").strip()

        try:
            menge = int(text)
        except ValueError:
            print("Eingabefehler: Bitte eine ganze Zahl eingeben (z.B. 1, 2, 3).")
            continue

        if menge <= 0:
            print("Eingabefehler: Menge muss größer als 0 sein.")
            continue

        return menge