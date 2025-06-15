# Hotel Reservation System

Dieses Projekt wurde im Rahmen des Moduls **„Anwendungsentwicklung mit Python“ (FS25)** an der FHNW umgesetzt. Ziel war es, ein funktionales Hotelreservierungssystem zu entwickeln, das Konzepte wie objektorientierte Programmierung, eine mehrschichtige Architektur und Datenbankzugriffe mit SQLite integriert und die vorgegebenen User Stories erfüllt.

---

## 1. Projektübersicht

Das System ermöglicht es Gästen, nach verfügbaren Hotels und Zimmern zu suchen, Buchungen vorzunehmen, zu stornieren und nach einem Aufenthalt Rechnungen zu erhalten. Gleichzeitig erhalten Administratoren umfassende Einsicht in alle Buchungen sowie die Möglichkeit, Hotels und Zimmerstammdaten zu verwalten.

**Ziel:** Entwicklung eines funktionalen Hotelreservierungssystems, das zentrale Prinzipien der Softwareentwicklung in Python vereint und die definierten User Stories vollständig abbildet.

**Technologien & Tools:**
- IDE: Visual Studio Code  
- Modellierung: Visual Paradigm  
- Versionskontrolle & Kollaboration: GitHub  

**Architektur (Schichtenmodell):**
- Model Layer – Domänenklassen: Hotel, Room, Guest, Booking, Invoice etc.  
- Data Access Layer (DAL) – Datenbankzugriffe via SQLite CRUD  
- Business Logic Layer (BLL) – Validierungen und Logik (Preis, Verfügbarkeit etc.)  
- UI Layer – Konsolenführung via `run.py`, Eingabe- und Validierungshelfer  
- User Stories – je Story ein Skript für gezieltes Testen

### Teamstruktur und besondere Situation:

Ursprünglich waren wir Teil einer vierköpfigen Gruppe. Im Laufe der Zusammenarbeit wurde jedoch klar, dass eine enge Kooperation in diesem Team nicht möglich war. Trotz anfänglicher Gespräche über gemeinsame Verantwortlichkeiten, stellte sich bald heraus, dass die Arbeits- und Kommunikationsstile zu unterschiedlich waren. Dies führte zu Missverständnissen, doppelten Aufgaben und fehlender Abstimmung.

Nach Rücksprache mit unserer Dozentin **Charuta** entschieden wir uns bewusst dazu, nicht gemeinsam weiterzuarbeiten. Stattdessen erhielten wir die Möglichkeit, ein separates, auf uns abgestimmtes Projekt abzugeben, das dieselben Kriterien erfüllte, aber ohne die Abhängigkeit von einem Team. Dies wurde ausdrücklich genehmigt und dokumentiert.

**Unsere alternative Vereinbarung beinhaltete:**
- Umsetzung aller **Minimal-User-Stories** eigenständig  
- Umsetzung einer **Erweiterung** (Datenbankschema oder Visualisierung)

Wir entschieden uns bewusst für die Erweiterung **„Visualisierung der Belegungsraten“**, da uns die Verbindung zu Datenanalyse und Reporting besonders interessierte und wir hier eigene Stärken einbringen konnten.

Trotz einiger technischer Einstiegshürden und neuem Rollenverständnis haben wir das Projekt schrittweise aufgebaut. Viele Komponenten – etwa DAO-Struktur, Validierungslogik und Rechnungsmodellierung – mussten wir selbst recherchieren und implementieren. In enger Abstimmung mit Charuta erhielten wir dazu gezieltes Feedback.

Ein besonderes Augenmerk legten wir auf die saubere Trennung der Schichten, die Wiederverwendbarkeit der Komponenten sowie die testbare Struktur unseres `run.py`-Menüs. Es erlaubt sowohl Admins als auch Gästen, gezielt über die Konsole durch das System zu navigieren.

Unser Ziel war es, ein kleines, aber vollständiges, gut getestetes und realitätsnahes System abzuliefern, das auf eigenen Entscheidungen, eigenem Verständnis und selbst erarbeiteter Logik basiert.

---

## 2. Aufgabenteilung

| Teammitglied | Zuständigkeiten |
|--------------|------------------|
| **David**    | Konsolenmenü, Eingabe-Logik, Teststruktur (run.py) |
| **Eufrat**   | Datenbankanbindung, Visualisierung, Preis- und Buchungslogik |
| **Beide**    | Struktur, User Stories, Dokumentation & Testing |

---

## 3. Klassendiagramm & Modellierung

Die objektorientierte Modellierung basiert auf einem vereinfachten ER-Diagramm mit zentralen Klassen wie Hotel, Room, Booking, Guest, RoomType etc. Diese wurden logisch in Python übertragen – mit besonderem Fokus auf Komposition, Aggregation und Kapselung. Das resultierende Klassendiagramm zeigt die Beziehung zwischen Entitäten und wurde mit Visual Paradigm erstellt.
![image](https://github.com/user-attachments/assets/4ef5068a-2656-42ad-8203-d434d4d85a8d)




---

## 4. Architektur & Aufbau

Die Ordnerstruktur folgt einer klaren Schichtenlogik:

```
📁 model/              # Datenmodelle (Hotel, Room, Guest...)
📁 data_access/        # DAO-Klassen für SQLite CRUD
📁 business_logic/     # Validierung, Preis, Verfügbarkeit
📁 ui/                 # run.py und Helfer für Konsoleneingabe
📁 database/           # SQLite-Initialisierung und DB-Files
📄 app.py              # Einstiegspunkt
```

Unsere Business-Logik ist so gestaltet, dass sie vollständig testbar ist, die DAOs sind eigenständig nutzbar und kapseln alle SQL-Befehle, während die Models rein datenhaltend bleiben.

---

## 5. Umgesetzte User Stories

- **US1:** Gäste können Hotels nach Stadt, Sternen, Verfügbarkeit filtern  
- **US2:** Zimmerdetails mit Beschreibung, Preis, Ausstattung anzeigen  
- **US3:** Admin kann Hotels hinzufügen, bearbeiten, löschen  
- **US4:** Gäste können Zimmer buchen (inkl. Validierung und Datum)  
- **US5:** Nach Buchung wird automatisch eine Rechnung erstellt  
- **US6:** Buchung kann storniert werden; Rechnung wird entfernt  
- **US7:** Zimmerpreise passen sich je nach Saison dynamisch an  
- **US8:** Admin erhält Übersicht über alle Buchungen  
- **US9 & US10:** Verwaltung von Zimmertypen, Ausstattung & Stammdaten (Teilimplementiert)

---

## 6. Erweiterung: Belegungsanalyse

Die Erweiterung visualisiert die Belegungsrate je Hotel und Zimmertyp. Sie wurde mit Hilfe von `pandas` umgesetzt und erlaubt eine tabellarische Übersicht über Auslastung pro Kategorie.

---

## 7. Herausforderungen

- Einstieg in SQLite & Datenmodellierung war aufwändig  
- Zirkuläre Importe und Klassenzuordnungen waren fehleranfällig  
- Preislogik (inkl. Hoch-/Nebensaison) erforderte viele Tests  
- Anpassung der Teamstruktur und Eigenverantwortung

---

## 8. Was wir gelernt haben

Während der Umsetzung dieses Projekts haben wir nicht nur unser technisches Know-how ausgebaut, sondern auch ein tieferes Verständnis für strukturiertes Arbeiten, sauberen Codeaufbau und Selbstorganisation gewonnen. Nachfolgend unsere wichtigsten Erkenntnisse:

### Datenstrukturierung aus der Praxis

- Die Übertragung eines ER-Diagramms in ein objektbasiertes Klassensystem war herausfordernd, aber zentral für den Projekterfolg.
- Klassen wie `Booking`, `Invoice` oder `RoomType` halfen uns, logische Zusammenhänge in Code zu übersetzen.
- Wir erkannten, wie nützlich Komposition und Aggregation sind, um abhängige Objekte wie Rechnungen automatisch zu erzeugen oder zu löschen.

### Strukturiertes Arbeiten mit Python

- Wir nutzten konsequent Objektorientierung: Konstruktoren, private Attribute, Assoziationen und Methoden wie `add_room()` oder `cancel_booking()`.
- Die Trennung zwischen Datenhaltung (Model) und Logik (BLL) hat sich im Verlauf mehrfach als hilfreich erwiesen.
- Besonders bei der Rechnungs- und Preislogik merkten wir, wie wichtig es ist, Verantwortlichkeiten im Code sauber zu trennen.

### GitHub im echten Teamprozess

- Durch das Arbeiten mit GitHub verstanden wir, wie wichtig Versionierung und Commit-Strukturen sind.
- Wir testeten und setzten Branches korrekt ein – inkl. Konfliktlösung bei Überschneidungen.
- Änderungen mussten wir oft zurücknehmen und systematisch neu einarbeiten – was unser Verständnis für „Codequalität“ stark geschärft hat.

### Eigenständige Organisation

- Durch die bewusste Trennung vom ursprünglichen Team lernten wir, Verantwortung für Architektur, Story-Umsetzung und Dokumentation zu übernehmen.
- Wir legten Wert auf klare Kommunikation und strukturierten Fortschritt – was uns half, jederzeit den Überblick zu behalten.
- Feedbackgespräche mit der Dozentin Charuta halfen uns, unsere Lösungen fachlich fundiert auszurichten.

### Aufbau & Testbarkeit

- Unser zentrales Menüsystem (`run.py`) wurde so konzipiert, dass alle Funktionen modular und unabhängig aufrufbar sind.
- Validierungshilfen (`input_helper.py`, `validation_helper.py`) sorgten für einheitliche Benutzerführung.
- Die Dateistruktur war so gewählt, dass sowohl Testing als auch Erweiterungen (z. B. Visualisierung) ohne größere Umbauten möglich waren.
- Durch saubere DAO-Klassen konnten wir Datenbankoperationen leicht isolieren und testen.

---

**Fazit:**  
Dieses Projekt hat uns gezeigt, wie wertvoll es ist, selbstständig eine vollständige Anwendung zu entwerfen – von der Datenstruktur bis zum Testmenü. Dabei waren nicht nur technische Fähigkeiten, sondern auch Planung, Reflexion und Disziplin gefragt.
