# Personendaten-Verwalter 

Eine moderne Desktop-Anwendung zur Verwaltung von Personendaten, entwickelt mit **Python** und **PyQt6**. Die Benutzeroberfläche bietet eine übersichtliche Tabellenansicht auf der linken Seite sowie ein komfortables Eingabeformular mit integriertem Kalender-Widget auf der rechten Seite.

##  Funktionen

- **Tabellenansicht:** Zeigt alle erfassten Personen mit ID, Vorname, Nachname, E-Mail, Geburtsdatum und Rolle an (inklusive flexibler Spaltenanpassung).
- **Datensätze verwalten:** 
  - **Speichern:** Validiert Pflichtfelder und fügt neue Datensätze automatisch mit fortlaufender ID hinzu.
  - **Neu:** Setzt das Eingabeformular zurück.
  - **Löschen:** Entfernt ausgewählte Zeilen direkt aus der Tabelle.
- **Eingabevalidierung & Statusleiste:** Gibt Echtzeit-Feedback und Statusmeldungen direkt am unteren Fensterrand aus.
- **Deutscher Kalender-Picker:** Integriertes `QDateEdit`-Widget mit deutscher Lokalisierung (`de_DE`), optimierter Breite und modernem Custom-Styling.
- **Datei-Dialoge & Formatauswahl:** Voll funktionsfähige Werkzeugleiste für *Öffnen*, *Speichern*, *Importieren* und *Exportieren* mit flexibler Formatauswahl (`CSV`, `JSON`, `XML`).

## Voraussetzungen

- **Python** 
- **PyQt6**

