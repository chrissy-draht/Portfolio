# Mitarbeiter-Datenbank

Dieses Projekt wurde im Rahmen meiner Umschulung zur Fachinformatikerin für Anwendungsentwicklung erstellt.

## Ziel
Aufbau einer relationalen Datenbank zur Verwaltung von Mitarbeitern und Abteilungen sowie Dokumentation eines vollständigen Entwicklungs- und Änderungsprozesses.

## Inhalte
- Erstellung der Tabellen „Mitarbeiter“ und „Abteilung“
- Festlegung sinnvoller Datentypen
- Nutzung von Primary Keys
- Aufbau und Auflösung von Foreign-Key-Beziehungen
- Erweiterung der Tabellenstruktur (z. B. zusätzliche Attribute)
- Einfügen, Aktualisieren und Löschen von Daten
- Durchführung verschiedener SQL-Abfragen
- Dokumentation der Entwicklungsschritte in einem ausführbaren SQL-Skript

## Technologien
- MySQL / MariaDB  
- SQL  
- phpMyAdmin  
- XAMPP (lokale Entwicklungsumgebung)  
- Visual Studio Code  

## Gelernt
- Grundlagen des Datenbankdesigns  
- Strukturierung relationaler Tabellen  
- Beziehungen zwischen Tabellen  
- Nutzung von Primär- und Fremdschlüsseln  
- Erweiterung und Anpassung bestehender Datenbankschemata  
- Durchführung typischer SQL-Abfragen  
  - Filter (WHERE, LIKE, BETWEEN)  
  - Sortierung (ORDER BY)  
  - Aggregationen (AVG, ROUND)  
  - JOIN-Abfragen  
- Fehleranalyse und schrittweise Korrektur von SQL-Befehlen  
- Dokumentation eines Entwicklungsprozesses von der ersten Idee bis zum finalen Zustand  

## Aufgabenstellung
Im Rahmen der Umschulung wurde eine relationale Datenbank zur Verwaltung von Mitarbeitern und Abteilungen erstellt.  
Dabei wurden folgende Anforderungen umgesetzt:

- Planung und Aufbau der Tabellenstruktur  
- Definition geeigneter Datentypen  
- Implementierung von Primary Keys und Foreign Keys  
- Erweiterung der Tabellen um zusätzliche Attribute  
- Einfügen und Bearbeiten von Beispiel-Datensätzen  
- Durchführung und Auswertung verschiedener SQL-Abfragen  
  - Sortierung und Filterung  
  - LIKE-Abfragen  
  - Durchschnittsberechnung  
  - Gehaltsanpassungen  
- Testen von Änderungen an der Struktur (ALTER TABLE)  
- Entfernen von Beziehungen und Tabellen zur Simulation von Änderungsprozessen  

## 📁 Code
Die vollständige SQL-Datei mit allen Entwicklungsschritten findest du hier:  
[session_script.sql](./session_script.sql)

Zusätzlich ist ein Export der Datenbank enthalten:  
[export_phpmyadmin.sql](./export_phpmyadmin.sql)

## Erweiterungsmöglichkeiten
- Entwicklung einer Benutzeroberfläche (z. B. Python oder Web)  
- Automatisierung von SQL-Prozessen  
- Integration in ein ERP-System  
- Erweiterung um weitere Entitäten (z. B. Projekte, Kunden, Rollen)  
- Umsetzung von Stored Procedures und Triggern  
