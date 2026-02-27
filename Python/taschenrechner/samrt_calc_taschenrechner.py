# ==================================================
# SMARTCALC - Konsolen-Taschenrechner
# ==================================================

print("=" * 40)
print("        SMARTCALC - TASCHENRECHNER")
print("=" * 40)

name = input("Wie heißt du? ")
print("\nHallo " + name + "!")
print("-" * 40)


# --------------------------------------------------
# Hilfsfunktion: Zahl einlesen (Komma erlaubt)
# --------------------------------------------------

def eingabe_zahl(prompt_text):
    original = input(prompt_text)
    umgewandelt = original.replace(",", ".")
    return original, float(umgewandelt)


nochmal = "j"

while nochmal == "j":

    print("\nWähle eine Operation:")
    print("  1 ➜  Addition")
    print("  2 ➜  Subtraktion")
    print("  3 ➜  Multiplikation")
    print("  4 ➜  Division")
    print("-" * 40)

    while True:
        auswahl = input("Deine Wahl (1-4): ")
        if auswahl in ["1", "2", "3", "4"]:
            break
        print("Ungültige Eingabe! Bitte nur 1, 2, 3 oder 4 eingeben.")

    # Originaltext + Float-Wert speichern
    zahl1_text, zahl1 = eingabe_zahl("Erste Zahl: ")
    zahl2_text, zahl2 = eingabe_zahl("Zweite Zahl: ")

    print("\n" + "-" * 40)

    if auswahl == "1":
        ergebnis = zahl1 + zahl2
        print("   " + zahl1_text + " + " + zahl2_text +
              " = " + format(ergebnis, ".2f"))

    elif auswahl == "2":
        ergebnis = zahl1 - zahl2
        print("   " + zahl1_text + " - " + zahl2_text +
              " = " + format(ergebnis, ".2f"))

    elif auswahl == "3":
        ergebnis = zahl1 * zahl2
        print("   " + zahl1_text + " * " + zahl2_text +
              " = " + format(ergebnis, ".2f"))

    elif auswahl == "4":
        if zahl2 == 0:
            print("   Division durch 0 ist nicht erlaubt!")
        else:
            ergebnis = zahl1 / zahl2
            print("   " + zahl1_text + " / " + zahl2_text +
                  " = " + format(ergebnis, ".2f"))

    print("-" * 40)

    nochmal = input("Nochmal rechnen? (j/n): ").lower()  # .lower = Großschreibung abfangen

print("\nProgramm beendet.")
print("=" * 40)