# SmartCalc – Konsolen-Taschenrechner

Dieses Projekt wurde im Rahmen meiner Umschulung zur Fachinformatikerin für Anwendungsentwicklung erstellt.

---

## Ziel

Entwicklung einer strukturierten Konsolenanwendung in Python, die:

- einen Benutzer begrüßt
- einfache Rechenoperationen ausführt
- Benutzereingaben validiert
- Dezimalzahlen mit Komma oder Punkt akzeptiert
- Ergebnisse korrekt auf zwei Nachkommastellen ausgibt
- Division durch 0 verhindert
- eine saubere und strukturierte Konsolenausgabe darstellt

---

## Inhalte

- Einlesen von Benutzereingaben (`input`)
- Arbeiten mit Datentypen (`float`, `string`)
- Umwandlung von Komma zu Punkt bei Dezimalzahlen
- Verwendung von `if / elif / else`
- Eingabevalidierung mit Schleifen
- Formatierung von Zahlen mit `format(..., ".2f")`
- Strukturierte Programmkommentierung
- Wiederholungsschleife für mehrere Berechnungen

---

## Funktionsumfang

### Teil A – Begrüßung
- Abfrage des Benutzernamens
- Strukturierte Ausgabe

### Teil B – Menü
- Auswahl zwischen:
  - Addition
  - Subtraktion
  - Multiplikation
  - Division
- Eingabevalidierung (nur 1–4 erlaubt)

### Teil C – Zahlenverarbeitung
- Akzeptiert Dezimalzahlen mit:
  - Punkt (z. B. 7.88)
  - Komma (z. B. 7,88)
- Interne Umwandlung für korrekte Berechnung

### Teil D – Berechnung
- Durchführung der gewählten Operation
- Division durch 0 wird abgefangen

### Teil E – Ausgabe
- Ergebnis wird auf zwei Nachkommastellen gerundet
- Eingabewerte bleiben unverändert dargestellt

### Teil F – Wiederholung
- Benutzer kann weitere Berechnungen durchführen

---

## Technologien

- Python 3
- Konsole (Terminal)
- Visual Studio Code

---

## Gelernt

- Strukturierte Programmierung
- Eingabevalidierung mit Schleifen
- Arbeiten mit Funktionen
- Umgang mit Fließkommazahlen
- Formatierung von Zahlen
- Fehlervermeidung (Division durch 0)
- Benutzerfreundliche Konsolenausgabe

---

## Code

Die vollständige Python-Datei befindet sich hier:

[samrt_calc_taschenrechner.py](samrt_calc_taschenrechner.py)

---

## Erweiterungsmöglichkeiten

- Potenzrechnung ergänzen
- Quadratwurzel integrieren
- Historie der Berechnungen speichern
- Export der Berechnung in eine Textdatei
- Umstellung auf objektorientierte Struktur
- Integration in eine grafische Benutzeroberfläche (z. B. mit Tkinter)

---