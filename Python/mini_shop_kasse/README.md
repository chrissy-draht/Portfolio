# Mini-Shop-Kasse mit Rabatt & Quittung

Dieses Projekt wurde im Rahmen meiner Umschulung zur Fachinformatikerin für Anwendungsentwicklung erstellt.

## Ziel

Entwicklung einer Konsolenanwendung in Python, die:

- mehrere Artikel erfasst  
- verschiedene Rabattarten verarbeitet  
- Zahlungsaufschläge berechnet  
- das Budget überprüft  
- eine strukturierte Quittung ausgibt  

---

## Inhalte

- Einlesen von Benutzereingaben (input)
- Arbeiten mit Datentypen (float, int, string)
- Berechnungen mit Zwischensumme und Endsumme
- Verwendung von if / elif / else
- Plausibilitätsprüfungen
- Formatierte Ausgabe mit f-Strings
- Runden von Geldbeträgen
- Strukturierte Konsolen-Ausgabe

---

## Funktionsumfang

### Teil A – Start & Budget
- Begrüßung des Kunden
- Abfrage des Budgets

### Teil B – Artikel erfassen
- Eingabe von 3 Artikeln
- Berechnung der Positionspreise
- Bildung einer Zwischensumme
- Validierung auf positive Preise und Mengen

### Teil C – Rabatt-Auswahl
- Kein Rabatt  
- Student (10%)  
- VIP (15%)  
- Gutschein (5€ ab 20€ Mindestwert)  

### Teil D – Extra-Rabatt
- 3% zusätzlicher Rabatt bei Gesamtmenge > 10

### Teil E – Zahlungsart
- Bar (kein Aufschlag)  
- Karte (+1%)  
- Online (+2%)  

### Teil F – Budgetprüfung
- Vergleich Endsumme mit Budget
- Ausgabe: OK oder NICHT GENUG GELD

---

## Technologien

- Python 3
- Konsole (Terminal)
- Visual Studio Code

---

## Gelernt

- Rechnen mit Variablen
- Strukturierte Programmierung
- Mehrfache Verzweigungen
- Plausibilitätsprüfungen
- Prozentberechnungen
- Saubere Konsolenausgabe

---

## Code

Die vollständige Python-Datei findest du hier:

[mini_shop_kasse.py](./mini_shop_kasse.py)

---

## Erweiterungsmöglichkeiten

- Unbegrenzte Anzahl an Artikeln (Schleife)
- Speichern der Quittung in einer Datei
- Grafische Benutzeroberfläche (z. B. mit Tkinter)
- Integration in ein Web-Frontend
