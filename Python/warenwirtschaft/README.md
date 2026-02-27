# Warenwirtschaft – Rechnungsprogramm (Konsole)

Dieses Projekt wurde im Rahmen meiner Umschulung zur Fachinformatikerin für Anwendungsentwicklung erstellt.

Ziel ist die Entwicklung eines konsolenbasierten Rechnungsprogramms mit strukturierter Programmierung und ausgelagerten Funktionen.

---

## Projektbeschreibung

Das Programm erstellt eine Rechnung auf Basis einer vorgegebenen Artikelliste.

Der Benutzer kann:

- Artikelnummern eingeben
- Die gekaufte Menge angeben
- Mehrere Positionen erfassen
- Die Eingabe mit 0 beenden

Das Programm berechnet:

- Netto-Gesamtsumme
- Umsatzsteuer (19 %)
- Bruttobetrag
- Bruttobetrag zusätzlich in DM

Eingabefehler werden abgefangen und führen zu einer Wiederholung der Eingabe.

---

## Artikelliste

| Artikelnummer | Artikel     | Netto-Preis (EUR) |
|--------------|------------|------------------|
| 17           | Bleistift  | 2.20             |
| 22           | Ordner     | 24.50            |
| 38           | USB-Stick  | 15.00            |
| 47           | Maus       | 9.95             |
| 125          | Tastatur   | 12.95            |

---

## Projektstruktur

```
warenwirtschaft/
│
├── main.py      # Hauptprogramm
└── b43.py       # Modul mit Eingabeprüfungen
```

### main.py
- Steuerung des Programms
- Berechnung von Netto, USt und Brutto
- Formatierte Ausgabe der Rechnung

### b43.py
- Eingabe der Artikelnummer (mit Validierung)
- Eingabe der Menge (mit Validierung)

---

## Programm starten

Im Terminal in den Projektordner wechseln:

cd warenwirtschaft
python main.py

---

## Verwendete Konzepte

- Funktionen
- Modul-Import
- Dictionaries
- Schleifen (while)
- Bedingungen (if / else)
- Eingabevalidierung mit try/except
- Formatierte Konsolenausgabe
- Prozentrechnung
- Währungsumrechnung (EUR → DM)

---

## Lernziele

- Strukturierung von Programmen
- Auslagerung von Funktionen in Module
- Benutzerfreundliche Konsolenausgabe
- Fehlerbehandlung
- Umsetzung eines praxisnahen Rechnungsprogramms

---

## Erweiterungsmöglichkeiten

- Automatische Rechnungsnummer
- Datum einfügen
- Speicherung der Rechnung als Datei
- Variable Umsatzsteuersätze (z. B. 7 % / 19 %)
- Erweiterung der Artikelliste
- Umsetzung als grafische Benutzeroberfläche

---

## Technologien

- Python 3
- Visual Studio Code
- Windows PowerShell