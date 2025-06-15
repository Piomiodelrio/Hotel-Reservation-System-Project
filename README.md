Hotel Reservation System
Dieses Projekt wurde im Rahmen des Moduls „Anwendungsentwicklung mit Python“ (FS25) an der FHNW umgesetzt. Ziel war es, ein funktionales Hotelreservierungssystem zu entwickeln, das Konzepte wie objektorientierte Programmierung, eine mehrschichtige Architektur und Datenbankzugriffe mit SQLite integriert und die vorgegebenen User Stories erfüllt.

1. Projektübersicht
Das System ermöglicht es Gästen, nach verfügbaren Hotels und Zimmern zu suchen, Buchungen vorzunehmen, zu stornieren und nach einem Aufenthalt Rechnungen zu erhalten. Gleichzeitig erhalten Administratoren umfassende Einsicht in alle Buchungen sowie die Möglichkeit, Hotels und Zimmerstammdaten zu verwalten.

Ziel: Entwicklung eines funktionalen Hotelreservierungssystems, das zentrale Prinzipien der Softwareentwicklung in Python vereint und die definierten User Stories vollständig abbildet.

Technologien & Tools:

IDE: Visual Studio Code

Modellierung: Visual Paradigm

Versionskontrolle & Kollaboration: GitHub

Architektur (Schichtenmodell):

Model Layer – Domänenklassen: Hotel, Room, Guest, Booking, Invoice etc.

Data Access Layer (DAL) – Datenbankzugriffe via SQLite CRUD

Business Logic Layer (BLL) – Validierungen und Logik (Preis, Verfügbarkeit etc.)

UI Layer – Konsolenführung via run.py, Eingabe- und Validierungshelfer

User Stories – je Story ein Skript für gezieltes Testen

Teamstruktur und besondere Situation:
Ursprünglich waren wir Teil einer vierköpfigen Gruppe. Im Laufe der Zusammenarbeit wurde jedoch klar, dass eine enge Kooperation in diesem Team nicht möglich war. Trotz anfänglicher Gespräche über gemeinsame Verantwortlichkeiten, stellte sich bald heraus, dass die Arbeits- und Kommunikationsstile zu unterschiedlich waren. Dies führte zu Missverständnissen, doppelten Aufgaben und fehlender Abstimmung.

Nach Rücksprache mit unserer Dozentin Charuta entschieden wir uns bewusst dazu, nicht gemeinsam weiterzuarbeiten. Stattdessen erhielten wir die Möglichkeit, ein separates, auf uns abgestimmtes Projekt abzugeben, das dieselben Kriterien erfüllte, aber ohne die Abhängigkeit von einem Team. Dies wurde ausdrücklich genehmigt und dokumentiert.

Unsere alternative Vereinbarung beinhaltete:

Umsetzung aller Minimal-User-Stories eigenständig

Umsetzung einer Erweiterung (Datenbankschema oder Visualisierung)

Wir entschieden uns bewusst für die Erweiterung „Visualisierung der Belegungsraten“, da uns die Verbindung zu Datenanalyse und Reporting besonders interessierte und wir hier eigene Stärken einbringen konnten.

Trotz einiger technischer Einstiegshürden und neuem Rollenverständnis haben wir das Projekt schrittweise aufgebaut. Viele Komponenten – etwa DAO-Struktur, Validierungslogik und Rechnungsmodellierung – mussten wir selbst recherchieren und implementieren. In enger Abstimmung mit Charuta erhielten wir dazu gezieltes Feedback.

Ein besonderes Augenmerk legten wir auf die saubere Trennung der Schichten, die Wiederverwendbarkeit der Komponenten sowie die testbare Struktur unseres run.py-Menüs. Es erlaubt sowohl Admins als auch Gästen, gezielt über die Konsole durch das System zu navigieren.

Unser Ziel war es, ein kleines, aber vollständiges, gut getestetes und realitätsnahes System abzuliefern, das auf eigenen Entscheidungen, eigenem Verständnis und selbst erarbeiteter Logik basiert.

2. Aufgabenteilung
Teammitglied	Zuständigkeiten
David	Konsolenmenü, Eingabe-Logik, Teststruktur (run.py)
Eufrat	Datenbankanbindung, Visualisierung, Preis- und Buchungslogik
Beide	Struktur, User Stories, Dokumentation & Testing

3. Klassendiagramm & Modellierung
Die objektorientierte Modellierung basiert auf einem vereinfachten ER-Diagramm mit zentralen Klassen wie Hotel, Room, Booking, Guest, RoomType etc. Diese wurden logisch in Python übertragen – mit besonderem Fokus auf Komposition, Aggregation und Kapselung. Das resultierende Klassendiagramm zeigt die Beziehung zwischen Entitäten und wurde mit Visual Paradigm erstellt.

(Siehe Klassendiagramm im GitHub-Ordner oder in der Abgabedokumentation.)

4. Architektur & Aufbau
Die Ordnerstruktur folgt einer klaren Schichtenlogik:

bash
Kopieren
Bearbeiten
📁 model/              # Datenmodelle (Hotel, Room, Guest...)
📁 data_access/        # DAO-Klassen für SQLite CRUD
📁 business_logic/     # Validierung, Preis, Verfügbarkeit
📁 ui/                 # run.py und Helfer für Konsoleneingabe
📁 database/           # SQLite-Initialisierung und DB-Files
📄 app.py              # Einstiegspunkt
Unsere Business-Logik ist so gestaltet, dass sie vollständig testbar ist, die DAOs sind eigenständig nutzbar und kapseln alle SQL-Befehle, während die Models rein datenhaltend bleiben.

5. Umgesetzte User Stories
US1: Gäste können Hotels nach Stadt, Sternen, Verfügbarkeit filtern

US2: Zimmerdetails mit Beschreibung, Preis, Ausstattung anzeigen

US3: Admin kann Hotels hinzufügen, bearbeiten, löschen

US4: Gäste können Zimmer buchen (inkl. Validierung und Datum)

US5: Nach Buchung wird automatisch eine Rechnung erstellt

US6: Buchung kann storniert werden; Rechnung wird entfernt

US7: Zimmerpreise passen sich je nach Saison dynamisch an

US8: Admin erhält Übersicht über alle Buchungen

US9 & US10: Verwaltung von Zimmertypen, Ausstattung & Stammdaten (Teilimplementiert)

6. Erweiterung: Belegungsanalyse
Die Erweiterung visualisiert die Belegungsrate je Hotel und Zimmertyp. Sie wurde mit Hilfe von pandas umgesetzt und erlaubt eine tabellarische Übersicht über Auslastung pro Kategorie.

7. Herausforderungen
Einstieg in SQLite & Datenmodellierung war aufwändig

Zirkuläre Importe und Klassenzuordnungen waren fehleranfällig

Preislogik (inkl. Hoch-/Nebensaison) erforderte viele Tests

Anpassung der Teamstruktur und Eigenverantwortung

8. Lessons Learned
Wir haben gelernt:

wie man aus einem ER-Modell eine objektorientierte Architektur baut

wie man Schichten entkoppelt und testbar gestaltet

wie wichtig klare Verantwortlichkeiten und Absprachen sind

dass auch ein kleines, aber gut strukturiertes Projekt überzeugen kann

Unsere persönliche Entwicklung war uns besonders wichtig: Wir wollten unabhängig ein Projekt aufbauen, das in sich stimmig, sauber dokumentiert und ehrlich erarbeitet ist.

9. Projektstart & Nutzung
bash
Kopieren
Bearbeiten
python app.py
Menü wählen (Gast / Admin)

gewünschte Funktion ausführen (z. B. Buchen, Rechnung anzeigen)

10. Abgabe & Kontakt
Abgabe: 15. Juni 2025

Modul: Anwendungsentwicklung mit Python

Team: David & Eufrat (FHNW, Business Artificial Intelligence)

Deepnote: siehe Link oben

GitHub-Link / Video-Link: werden ergänzt

