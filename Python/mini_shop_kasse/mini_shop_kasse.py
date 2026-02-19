# Projekt Mini Shop-Kasse mit Rabatt & Quittung
 
print("Herzlich Willkommen im Mini-Shop!")

kunde = input("Wie heißt du?: ")
print("Hallo", kunde, ", schön dass du da bist")

budget = float(input("Wie hoch ist dein Budget für den heutigen Einkauf (z.B. 50.00EUR): ").replace(",", "."))

zwischensumme = 0.0

######################################################
# Teil B: 3 Artikel

# Artikel 1
artikel1 = input("\nWas ist dein erster Artikel: ")
preis1 = float(input("Stückpreis für Artikel 1 ist: ").replace(",", "."))
menge1 = int(input("Menge Artikel 1: "))

if preis1 <= 0 or menge1 <= 0:
    print("Ungültige Eingabe. Es gibt nur positive Preise und Mengen.")
    exit()

pos1 = preis1 * menge1
zwischensumme = zwischensumme + pos1
print("Hinzugefügt wurde:", artikel1, "|", f"{preis1:.2f}", "€ x", menge1, "=", f"{pos1:.2f}", "€")

# Artikel 2
artikel2 = input("\nWas ist dein zweiter Artikel: ")
preis2 = float(input("Stückpreis für Artikel 2 ist: ").replace(",", "."))
menge2 = int(input("Menge Artikel 2: "))

if preis2 <= 0 or menge2 <= 0:
    print("Ungültige Eingabe. Es gibt nur positive Preise und Mengen.")
    exit()

pos2 = preis2 * menge2
zwischensumme = zwischensumme + pos2
print("Hinzugefügt wurde:", artikel2, "|", f"{preis2:.2f}", "€ x", menge2, "=", f"{pos2:.2f}", "€")

# Artikel 3
artikel3 = input("\nWas ist dein dritter Artikel: ")
preis3 = float(input("Stückpreis für Artikel 3 ist: ").replace(",", "."))
menge3 = int(input("Menge Artikel 3: "))

if preis3 <= 0 or menge3 <= 0:
    print("Ungültige Eingabe. Es gibt nur positive Preise und Mengen.")
    exit()

pos3 = preis3 * menge3
zwischensumme = zwischensumme + pos3
print("Hinzugefügt wurde:", artikel3, "|", f"{preis3:.2f}", "€ x", menge3, "=", f"{pos3:.2f}", "€")

##################################################
# Teil C: Rabatt auswählen

print("\nRabatt auswählen:")
print("1 = Kein Rabatt")
print("2 = Student 10% Rabatt")
print("3 = VIP 15% Rabatt")
print("4 = Gutschein 5€ (nur wenn Zwischensumme >= 20€)")

rabatt_wahl = int(input("Dein Rabatt (1-4): "))

rabatt_betrag = 0.0
rabatt_text = "Kein Rabatt"

if rabatt_wahl == 1:
    rabatt_text = "Kein Rabatt"
    rabatt_betrag = 0.0

elif rabatt_wahl == 2:
    rabatt_text = "Student 10%"
    rabatt_betrag = zwischensumme * 0.10

elif rabatt_wahl == 3:
    rabatt_text = "VIP 15%"
    rabatt_betrag = zwischensumme * 0.15

elif rabatt_wahl == 4:
    if zwischensumme >= 20:
        rabatt_text = "Gutschein 5€"
        rabatt_betrag = 5.0
    else:
        rabatt_text = "Gutschein (nicht angewendet)"
        rabatt_betrag = 0.0
        print("Zwischensumme zu niedrig (unter 20€) – Gutschein nicht anwendbar.")

else:
    print("Ungültige Auswahl beim Rabatt.")
    exit()

##################################################
# Bonus: Extra-Rabatt, wenn Gesamtmenge > 10

extra_rabatt = "Kein extra Rabatt"
extrabetrag = 0.0

gesamtmenge = menge1 + menge2 + menge3

if gesamtmenge > 10:
    extra_rabatt = "Extra Rabatt 3% (Menge > 10)"
    extrabetrag = zwischensumme * 0.03

##################################################
# Summe nach Rabatt

summe_nach_rabatt = zwischensumme - rabatt_betrag - extrabetrag

if summe_nach_rabatt < 0:
    summe_nach_rabatt = 0.0

##################################################
# Bonus: Zahlungsart (Aufschlag NACH Rabatt)

print("\nZahlungsart auswählen:")
print("1 = Bar (kein Aufschlag)")
print("2 = Karte (+1%)")
print("3 = Online (+2%)")

zahlungsart = int(input("Deine Zahlungsart (1-3): "))

aufschlag_text = "kein Aufschlag"
aufschlag_betrag = 0.0

if zahlungsart == 1:
    aufschlag_text = "Bar (0%)"
    aufschlag_betrag = 0.0

elif zahlungsart == 2:
    aufschlag_text = "Karte (+1%)"
    aufschlag_betrag = summe_nach_rabatt * 0.01

elif zahlungsart == 3:
    aufschlag_text = "Online (+2%)"
    aufschlag_betrag = summe_nach_rabatt * 0.02

else:
    print("Ungültige Zahlungsart.")
    exit()

##################################################
# Endsumme + Runden

endsumme = summe_nach_rabatt + aufschlag_betrag
endsumme = round(endsumme, 2)

restbudget = round(budget - endsumme, 2)

##################################################
# Budget-Check

if endsumme > budget:
    status = "NICHT GENUG GELD"
else:
    status = "OK"

##################################################
# Quittung (schöne Ausgabe)

print("\n========== QUITTUNG ==========")
print("Kunde:", kunde)
print("\nArtikel:")
print("1)", artikel1 + ":", f"{preis1:.2f}€ x {menge1} = {pos1:.2f}€")
print("2)", artikel2 + ":", f"{preis2:.2f}€ x {menge2} = {pos2:.2f}€")
print("3)", artikel3 + ":", f"{preis3:.2f}€ x {menge3} = {pos3:.2f}€")
print("=============================")
print("\nZwischensumme:", f"{zwischensumme:.2f}€\n")
print("=============================")
print("Rabatt (" + rabatt_text + "):", "-" + f"{rabatt_betrag:.2f}€")

if extrabetrag > 0:
    print(extra_rabatt + ":", "-" + f"{extrabetrag:.2f}€")


print("Aufschlag (" + aufschlag_text + "):", "+" + f"{aufschlag_betrag:.2f}€")
print("=============================")
print("Endsumme:", f"{endsumme:.2f}€")
print("=============================")
print("Budget:", f"{budget:.2f}€")
print("Restbudget:", f"{restbudget:.2f}€")
print("Status:", status)
print("=============================")



