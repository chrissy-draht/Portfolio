# main.py
# Rechnung (Warenwirtschaft)

from b43 import eingabe_artikelnummer, eingabe_menge

# Artikelliste: Artikelnummer -> (Artikelname, Netto-Einzelpreis EUR)
ARTIKEL = {
    17: ("Bleistift", 2.20),
    22: ("Ordner", 24.50),
    38: ("USB-Stick", 15.00),
    47: ("Maus", 9.95),
    125: ("Tastatur", 12.95)
}

UST_SATZ = 0.19          # 19% Umsatzsteuer
EUR_PRO_DM = 1.95583     # 1 EUR = 1.95583 DM


def drucke_preisliste():
    print("=" * 60)
    print("PREISLISTE")
    print("=" * 60)
    print("Art.-Nr | Artikel        | Netto-Preis (EUR)")
    print("-" * 60)

    # sortiert nach Artikelnummer
    for nr in sorted(ARTIKEL.keys()):
        name, preis = ARTIKEL[nr]
        print(
            str(nr).rjust(6), " | ",
            name.ljust(13), " | ",
            format(preis, ".2f").rjust(15)
        )

    print("=" * 60)


def main():
    drucke_preisliste()

    posten_liste = []  # speichert (artikelnummer, name, menge, einzelpreis, postenwert)
    netto_summe = 0.0

    artikelnummer = eingabe_artikelnummer(ARTIKEL)

    while artikelnummer != 0:
        name, einzelpreis = ARTIKEL[artikelnummer]
        menge = eingabe_menge()

        postenwert = einzelpreis * menge
        netto_summe = netto_summe + postenwert

        posten_liste.append((artikelnummer, name, menge, einzelpreis, postenwert))

        print("-" * 60)
        print("Posten:", name, "(" + str(artikelnummer) + ") x", menge,
              "=", format(postenwert, ".2f"), "EUR (netto)")
        print("-" * 60)

        artikelnummer = eingabe_artikelnummer(ARTIKEL)

    # Summen berechnen
    ust = netto_summe * UST_SATZ
    brutto = netto_summe + ust
    brutto_dm = brutto * EUR_PRO_DM

    # Rechnung ausgeben
    print("\n" + "=" * 60)
    print("RECHNUNG")
    print("=" * 60)

    if len(posten_liste) == 0:
        print("Keine Posten eingegeben.")
    else:
        print("Art.-Nr | Artikel        | Menge | Einzel | Posten (netto)")
        print("-" * 60)

        for art, name, menge, preis, wert in posten_liste:
            print(
                str(art).rjust(6), " | ",
                name.ljust(13), " | ",
                str(menge).rjust(5), " | ",
                format(preis, ".2f").rjust(6), " | ",
                format(wert, ".2f").rjust(12)
            )

        print("-" * 60)
        print("Netto: ", format(netto_summe, ".2f"), "EUR")
        print("USt (" + str(int(UST_SATZ * 100)) + "%):", format(ust, ".2f"), "EUR")
        print("Brutto:", format(brutto, ".2f"), "EUR")
        print("Brutto in DM:", format(brutto_dm, ".2f"), "DM")
        print("=" * 60)


if __name__ == "__main__":
    main()