# Warenwirtschaft – Rechnungsprogramm (Konsole)

Dieses Projekt entstand im Rahmen meiner Umschulung zur Fachinformatikerin für Anwendungsentwicklung.

Ziel war es, ein einfaches konsolenbasiertes Rechnungsprogramm zu entwickeln, das strukturiert aufgebaut ist und Funktionen in ein separates Modul auslagert.

---

## Projektbeschreibung

Das Programm erstellt eine Rechnung auf Grundlage einer festen Artikelliste.

Der Benutzer kann:

- Artikelnummern eingeben
- Die gewünschte Menge angeben
- Mehrere Positionen erfassen
- Die Eingabe mit 0 beenden

Nach Abschluss der Eingabe berechnet das Programm:

- die Netto-Gesamtsumme
- die Umsatzsteuer (19 %)
- den Bruttobetrag
- zusätzlich die Umrechnung des Bruttobetrags in DM

Fehleingaben werden geprüft und müssen bei Bedarf erneut eingegeben werden.

---

## Artikelliste

| Artikelnummer | Artikel     | Netto-Preis (EUR) |
|---------------|------------|-------------------|
| 17            | Bleistift  | 2.20              |
| 22            | Ordner     | 24.50             |
| 38            | USB-Stick  | 15.00             |
| 47            | Maus       | 9.95              |
| 125           | Tastatur   | 12.95             |

---

## Projektstruktur

```
warenwirtschaft/
│
├── main.py
└── b43.py
```

---

## Code-Dateien

- [main.py](main.py) – enthält die Programmsteuerung und die Berechnungslogik  
- [b43.py](./b43.py) – enthält die Eingabevalidierung für Artikelnummer und Menge  

---

## Programm starten

Im Terminal in den Projektordner wechseln:

```
cd warenwirtschaft
python main.py
```

---

## Verwendete Konzepte

- Funktionen
- Eigene Module (Import von Python-Dateien)
- Dictionaries zur Speicherung der Artikeldaten
- while-Schleifen
- if / else-Bedingungen
- try / except zur Fehlerbehandlung
- Formatierung von Zahlen
- Prozentrechnung
- Umrechnung von Euro in DM

---

## Lernziele

Mit diesem Projekt habe ich:

- Programme strukturiert aufgebaut
- Funktionen in separate Module ausgelagert
- Benutzereingaben geprüft
- Berechnungen korrekt umgesetzt
- eine übersichtliche Konsolenausgabe gestaltet

---

## Erweiterungsmöglichkeiten

- Automatische Vergabe einer Rechnungsnummer
- Einfügen des aktuellen Datums
- Speicherung der Rechnung als Textdatei
- Erweiterbare Artikelliste
- Umsetzung als grafische Benutzeroberfläche

---

## Technologien

- Python 3
- Visual Studio Code
- Windows PowerShell