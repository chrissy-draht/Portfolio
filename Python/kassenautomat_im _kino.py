# Projekt: Kassenautomat im Kino

TICKET_2D = 9.50
TICKET_3D = 12.00
SNACK_PRO_TICKET = 4.20
KARTENGEBUEHR_SATZ = 0.015

anz_bestellungen = 0
summe_tickets = 0
gesamteinnahmen = 0.0

weiter = "ja"

while weiter == "ja":

    name = input("Name: ")

# Alter (mit try/except + raise)
    alter_ok = False
    alter = 0
    while alter_ok == False:
        try:
            alter = int(input("Alter: "))
            if alter < 0 or alter > 120:
                raise ValueError("Unrealistisches Alter!")
            alter_ok = True
        except ValueError:
            print("Ungültige Eingabe beim Alter!")

    if alter < 6:
        print("Bestellung abgelehnt: Zu jung.")
        weiter = input("Weitere Bestellung? (ja/nein): ")
        continue

    filmtyp = input("Filmtyp (2D/3D): ")

# Ticketanzahl (mit try/except + raise)
    tickets_ok = False
    tickets = 0
    while tickets_ok == False:
        try:
            tickets = int(input("Anzahl Tickets: "))
            if tickets <= 0:
                raise ValueError("Ticketanzahl muss > 0 sein!")
            tickets_ok = True
        except ValueError:
            print("Ungültige Eingabe bei Ticketanzahl!")

    snack = input("Snack (ja/nein): ")
    zahlung = input("Zahlungsmethode (karte/bar): ")

# Ticketpreis je nach Filmtyp
    if filmtyp == "3D":
        einzelpreis = TICKET_3D
    else:
        einzelpreis = TICKET_2D

# Geschachtelte Verzweigung + logische Operatoren
    if filmtyp == "3D" and alter < 12:
        print("Warnung: 3D nur mit Begleitung empfohlen")
        if snack == "ja":
            print("Snack wird vorbereitet")

# Ticket-Zwischensumme
    ticket_summe = einzelpreis * tickets

# Rabatte
    senior_rabatt = 0.0
    mengen_rabatt = 0.0

    if alter >= 65:
        senior_rabatt = ticket_summe * 0.10

    if tickets >= 10:
        mengen_rabatt = ticket_summe * 0.10
    elif tickets >= 5:
        mengen_rabatt = ticket_summe * 0.05

    rabatt_gesamt = senior_rabatt + mengen_rabatt
    ticket_nach_rabatt = ticket_summe - rabatt_gesamt

# Snack-Kosten
    snack_kosten = 0.0
    if snack == "ja":
        snack_kosten = tickets * SNACK_PRO_TICKET

# Zwischensumme
    zwischensumme = ticket_nach_rabatt + snack_kosten

# Kartengebühr
    kartengebuehr = 0.0
    if zahlung == "karte":
        kartengebuehr = zwischensumme * KARTENGEBUEHR_SATZ

    endsumme = zwischensumme + kartengebuehr

# Ticket-Drucksimulation (for-Schleife)
    for i in range(1, tickets + 1):
        reihe = "A"
        print("Ticket", str(i) + "/" + str(tickets) + ":", filmtyp + " - Reihe", reihe)

# Rechnung (formatiert mit %)
    print()
    print("Kino-Kasse – Rechnung")
    print("Kunde:", name + " (Alter:", str(alter) + ")")
    print("Film:", filmtyp)
    print()
    print("%-28s %10s" % ("Position", "Betrag"))
    print("----------------------------------------")

    print("%-28s %10.2f" % ("Tickets (" + str(tickets) + " x " + ("%.2f" % einzelpreis) + "€)", ticket_summe))

    if senior_rabatt > 0:
        print("%-28s %10.2f" % ("Senior-Rabatt (10%)", -senior_rabatt))

    if mengen_rabatt > 0:
        if tickets >= 10:
            print("%-28s %10.2f" % ("Mengenrabatt (10%)", -mengen_rabatt))
        else:
            print("%-28s %10.2f" % ("Mengenrabatt (5%)", -mengen_rabatt))

    if snack_kosten > 0:
        print("%-28s %10.2f" % ("Snack (" + str(tickets) + " x 4.20€)", snack_kosten))

    if kartengebuehr > 0:
        print("%-28s %10.2f" % ("Kartengebühr (1.5%)", kartengebuehr))

    print("----------------------------------------")
    print("%-28s %10.2f" % ("Zu zahlen:", endsumme))
    print()

# Tages-Zusammenfassung sammeln
    anz_bestellungen += 1
    summe_tickets += tickets
    gesamteinnahmen += endsumme

    weiter = input("Weitere Bestellung? (ja/nein): ")

print()
print("===== Tageszusammenfassung =====")
print("Anzahl Bestellungen:", anz_bestellungen)
print("Summe Tickets:", summe_tickets)
print("Gesamteinnahmen: %.2f Euro" % gesamteinnahmen)
print("===============================")
