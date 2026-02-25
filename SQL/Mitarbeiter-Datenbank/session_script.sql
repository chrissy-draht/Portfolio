-- =========================================================
-- Chronologisches Script 
-- Datenbank: chrissy
-- =========================================================

-- 1) Datenbank erstellen & verwenden
CREATE DATABASE IF NOT EXISTS chrissy;
USE chrissy;

-- 2) Abteilung anlegen
CREATE TABLE IF NOT EXISTS Abteilung (
    AbteilungsID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL
);

-- 3) Mitarbeiter anlegen ohne AUTO_INCREMENT bei MitarbeiterID
CREATE TABLE IF NOT EXISTS Mitarbeiter (
    MitarbeiterID INT PRIMARY KEY,
    Nachname VARCHAR(50),
    Vorname VARCHAR(50),
    Gehalt DECIMAL(10,2) NOT NULL,
    AbteilungsID INT NULL,
    CONSTRAINT fk_mitarbeiter_abteilung
        FOREIGN KEY (AbteilungsID)
        REFERENCES Abteilung(AbteilungsID)
);

-- 4) Spalte Wohnort hinzufügen und vergrößern
ALTER TABLE Mitarbeiter ADD Wohnort VARCHAR(10);
ALTER TABLE Mitarbeiter MODIFY Wohnort VARCHAR(50);

-- 5) Ersten Mitarbeiter einfügen (ID 1)
INSERT INTO Mitarbeiter (MitarbeiterID, Nachname, Vorname, Gehalt, AbteilungsID, Wohnort)
VALUES (1, 'Müller', 'Klaus', 2500.00, NULL, NULL);

-- 6) Abteilung "Einkauf" (ID 1) einfügen
INSERT INTO Abteilung (AbteilungsID, Name)
VALUES (1, 'Einkauf');

-- 7) Weitere Mitarbeiter (IDs 2-4) einfügen (Wohnort mit korrekten Quotes)
INSERT INTO Mitarbeiter (MitarbeiterID, Nachname, Vorname, Gehalt, Wohnort)
VALUES
(2, 'Draht', 'Chrissy', 6000.00, 'Grabenstätt'),
(3, 'Rehm',  'Vic',    7500.00, 'Berlin'),
(4, 'Xaver', 'Zentrum',1500.00, 'Schneeberg');

-- 8) Abteilung "Buchhaltung" (ID 2) einfügen
INSERT INTO Abteilung (AbteilungsID, Name)
VALUES (2, 'Buchhaltung');

-- 9) AbteilungsID setzen (bei Rehm & Draht auf 2)
UPDATE Mitarbeiter
SET AbteilungsID = 2
WHERE Nachname IN ('Rehm', 'Draht');

-- 10) JOIN-Abfrage (Buchhaltung)
SELECT m.Nachname, m.Vorname
FROM Mitarbeiter m
JOIN Abteilung a ON a.AbteilungsID = m.AbteilungsID
WHERE a.Name = 'Buchhaltung';

-- 11) Gehalt zwischen 2000 und 2500
SELECT Nachname, Vorname, Gehalt
FROM Mitarbeiter
WHERE Gehalt BETWEEN 2000.00 AND 2500.00;

-- 12) Mitarbeiter ohne MitarbeiterID einfügen
INSERT INTO Mitarbeiter (Nachname, Vorname, Gehalt, AbteilungsID, Wohnort)
VALUES ('Schusi', 'Schmitt', 4000.00, 2, 'Doduhausen');

-- 13) Nachnamen wie "Sch%"
SELECT Nachname
FROM Mitarbeiter
WHERE Nachname LIKE 'Sch%';

-- 14) Hansmann & Manomann mit expliziten IDs (5,6) einfügen
INSERT INTO Mitarbeiter (MitarbeiterID, Nachname, Vorname, Gehalt, AbteilungsID, Wohnort)
VALUES
(5, 'Hansmann', 'Manfred', 1000.00, 1, 'Mannhausen'),
(6, 'Manomann', 'Herman',  8000.00, 1, 'Teuerhausen');

-- 15) Show databases (optional, nur Info)
-- SHOW DATABASES;

-- 16) Nachnamen wie "%mann%"
SELECT Nachname
FROM Mitarbeiter
WHERE Nachname LIKE '%mann%';

-- 17) Durchschnittsgehalt + Rundung
SELECT AVG(Gehalt) AS Bohne
FROM Mitarbeiter;

SELECT ROUND(AVG(Gehalt), 3) AS Bohne
FROM Mitarbeiter;

SELECT ROUND(AVG(Gehalt)) AS Bohne
FROM Mitarbeiter;

-- 18) Gehälter um 1,5% erhöhen
UPDATE Mitarbeiter
SET Gehalt = Gehalt * 1.015;

-- 19) Anton (ID 7) ohne Nachname einfügen, dann wieder löschen
INSERT INTO Mitarbeiter (MitarbeiterID, Vorname, Gehalt, AbteilungsID, Wohnort)
VALUES (7, 'Anton', 5000.00, 1, 'Aue');

DELETE FROM Mitarbeiter
WHERE Nachname IS NULL OR Nachname = '';

-- 20) Wohnort wieder entfernen
ALTER TABLE Mitarbeiter DROP COLUMN Wohnort;

-- 21) Foreign Key entfernen und Abteilungstabelle löschen
ALTER TABLE Mitarbeiter DROP FOREIGN KEY fk_mitarbeiter_abteilung;
DROP TABLE Abteilung;

-- Ergebnis am Ende:
-- - Datenbank chrissy existiert
-- - Tabelle Mitarbeiter existiert mit: MitarbeiterID, Nachname, Vorname, Gehalt, AbteilungsID
-- - Tabelle Abteilung existiert NICHT mehr
-- - Kein FK mehr
-- - Wohnort existiert NICHT mehr