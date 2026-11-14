from PyQt6.QtCore import QDate, QLocale, Qt
from PyQt6.QtWidgets import *

app = QApplication([])

window = QMainWindow()
window.setWindowTitle("Personendaten-Verwalter")
window.resize(1100, 600)

central_widget = QWidget()
central_widget.setStyleSheet("background-color: #e6f2ff;")
main_layout = QVBoxLayout(central_widget)

#===========================================================================
toolbar_layout = QHBoxLayout()
btn_open = QPushButton("📂\nÖffnen")
btn_save = QPushButton("💾 \nSpeichern")
btn_import = QPushButton("📥 \nImportieren")
btn_export = QPushButton("📤 \nExportieren")
btn_settings = QPushButton("⚙️ \nEinstellungen")

for btn in [btn_open, btn_save, btn_import, btn_export, btn_settings]:
  btn.setMinimumSize(80, 50)
  toolbar_layout.addWidget(btn)

toolbar_layout.addStretch()
format_label = QLabel("Format:")
format_combo = QComboBox()
format_combo.addItems(["CSV", "JSON", "XML"])
toolbar_layout.addWidget(format_label)
toolbar_layout.addWidget(format_combo)

main_layout.addLayout(toolbar_layout)

#===========================================================================
content_layout = QHBoxLayout()

# --- Left Side: Search & Table ---
left_layout = QVBoxLayout()
search_input = QLineEdit()
search_input.setPlaceholderText("Suche...")
left_layout.addWidget(search_input)

table = QTableWidget(6, 6)
table.setHorizontalHeaderLabels(
    ["ID", "Vorname", "Nachname", "E-Mail", "Geburtsdatum", "Rolle"]
)

header = table.horizontalHeader()
header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
header.setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)
header.setSectionResizeMode(2, QHeaderView.ResizeMode.Interactive)
header.setSectionResizeMode(
    3, QHeaderView.ResizeMode.Stretch
)  # E-Mail lesbar machen
header.setSectionResizeMode(4, QHeaderView.ResizeMode.Interactive)
header.setSectionResizeMode(5, QHeaderView.ResizeMode.Interactive)

table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
table.verticalHeader().setVisible(
    False
)  # Versteckt doppelte Standard-ID-Zeilen

# Sample Data
data = [
    ("1", "Adu", "Mearey", "adu@gmail.com", "12.05.2012", "Weiner"),
    ("2", "Dan", "Mearey", "Dan@gmail.com", "17.05.2005", "Personal"),
    ("3", "Danayt", "Mearey", "danayt@gmail.com", "12.08.1993", "Rolle"),
    ("4", "Delina", "Mearey", "delina@gmail.com", "07.09.1997", "Kategorier"),
    ("5", "Kah", "Mearey", "Kahm@gmail.com", "19.01.1998", "Rolle"),
    ("6", "Sami", "Mearey", "sami@gmail.com", "15.07.2010", "Kategorie"),
]

for row_idx, row_values in enumerate(data):
  for col_idx, value in enumerate(row_values):
    table.setItem(row_idx, col_idx, QTableWidgetItem(value))

left_layout.addWidget(table)
content_layout.addLayout(left_layout, 3)

#===========================================================================
right_layout = QVBoxLayout()
form_container = QWidget()
form_container.setStyleSheet(
    "border: 1px solid #dcdcdc; border-radius: 6px; background-color: #fafafa;"
    " padding: 10px;"
)
form_layout = QFormLayout(form_container)
form_title = QLabel("<b>Personendaten bearbeiten / hinzufügen</b>")
form_layout.addRow(form_title)

input_vorname = QLineEdit()
input_nachname = QLineEdit()
input_email = QLineEdit()

#===========================================================================
input_geburt = QDateEdit()
input_geburt.setCalendarPopup(True)
input_geburt.setDisplayFormat("dd.MM.yyyy")
input_geburt.setDate(QDate(2000, 1, 1))

cal = input_geburt.calendarWidget()
cal.setLocale(QLocale(QLocale.Language.German, QLocale.Country.Germany))
cal.setMinimumWidth(300)

#===========================================================================
input_geburt.setStyleSheet("""
    QDateEdit {
        background-color: #ffffff; 
        border: 1px solid #cbd5e1; 
        border-radius: 3px; 
        padding: 4px;
    }
    QCalendarWidget QWidget {
        background-color: #ffffff;
        color: #1e293b;
    }
    QCalendarWidget QWidget#qt_calendar_navigationbar {
        background-color: #f1f5f9;
        border-bottom: 1px solid #cbd5e1;
        padding: 6px;
    }
    QCalendarWidget QToolButton {
        background-color: #ffffff;
        color: #1e293b;
        font-weight: bold;
        border: 1px solid #cbd5e1;
        border-radius: 4px;
        margin: 2px;
        padding: 4px 8px;
    }
    QCalendarWidget QToolButton:hover {
        background-color: #e2eaf4;
        border-color: #3b82f6;
    }
    QCalendarWidget QMenu {
        background-color: #ffffff;
        color: #1e293b;
        border: 1px solid #cbd5e1;
    }
    QCalendarWidget QAbstractItemView:enabled {
        selection-background-color: #3b82f6;
        selection-color: #ffffff;
        color: #1e293b;
    }
""")

input_telefon = QLineEdit()
input_rolle = QComboBox()
input_rolle.addItems(["Weiner", "Personal", "Rolle", "Kategorier", "Kategorie"])

form_layout.addRow("Vorname", input_vorname)
form_layout.addRow("Nachname", input_nachname)
form_layout.addRow("E-Mail", input_email)
form_layout.addRow("Geburtsdatum", input_geburt)
form_layout.addRow("Telefon", input_telefon)
form_layout.addRow("Rolle/Kategorie", input_rolle)

right_layout.addWidget(form_container)
#===========================================================================
right_layout.addSpacing(145)
form_btn_layout = QHBoxLayout()
btn_neu = QPushButton("➕ Neu")
btn_speichern = QPushButton("💾 Speichern")
btn_loeschen = QPushButton("🗑️ Löschen")

btn_speichern.setStyleSheet(
    "background-color: #e2f0d9; color: #274e13; font-weight: bold;"
)
btn_loeschen.setStyleSheet(
    "background-color: #f4cccc; color: #660000; font-weight: bold;"
)

form_btn_layout.addWidget(btn_neu)
form_btn_layout.addWidget(btn_speichern)
form_btn_layout.addWidget(btn_loeschen)

right_layout.addLayout(form_btn_layout)
right_layout.addStretch()

content_layout.addLayout(right_layout, 2)
main_layout.addLayout(content_layout)

#===========================================================================
def daten_speichern():
  vorname = input_vorname.text().strip()
  nachname = input_nachname.text().strip()

  if not vorname or not nachname:
    window.statusBar().showMessage(
        "Bitte Vor- und Nachname eingeben!", 3000
    )
    return

  next_id = str(table.rowCount() + 1)
  email = input_email.text()
  geburt = input_geburt.date().toString("dd.MM.yyyy")
  rolle = input_rolle.currentText()

  row_idx = table.rowCount()
  table.insertRow(row_idx)

  table.setItem(row_idx, 0, QTableWidgetItem(next_id))
  table.setItem(row_idx, 1, QTableWidgetItem(vorname))
  table.setItem(row_idx, 2, QTableWidgetItem(nachname))
  table.setItem(row_idx, 3, QTableWidgetItem(email))
  table.setItem(row_idx, 4, QTableWidgetItem(geburt))
  table.setItem(row_idx, 5, QTableWidgetItem(rolle))

  neues_formular()
  window.statusBar().showMessage(
      f"Datensatz für {vorname} {nachname} gespeichert.", 3000
  )


def neues_formular():
  input_vorname.clear()
  input_nachname.clear()
  input_email.clear()
  input_telefon.clear()
  input_geburt.setDate(QDate(2000, 1, 1))
  input_rolle.setCurrentIndex(0)
  input_vorname.setFocus()


def daten_loeschen():
  current_row = table.currentRow()
  if current_row >= 0:
    table.removeRow(current_row)
    window.statusBar().showMessage("Ausgewählter Datensatz gelöscht.", 3000)
  else:
    window.statusBar().showMessage(
        "Bitte zuerst eine Zeile in der Tabelle auswählen!", 3000
    )


#===========================================================================
def datei_oeffnen():
  selected_format = format_combo.currentText()
  file_name, _ = QFileDialog.getOpenFileName(
      window,
      "Datei öffnen",
      "",
      f"{selected_format} Files (*.{selected_format.lower()});;All Files (*)",
  )
  if file_name:
    window.statusBar().showMessage(f"Datei geöffnet: {file_name}", 3000)


def datei_speichern_dialog():
  selected_format = format_combo.currentText()
  file_name, _ = QFileDialog.getSaveFileName(
      window,
      "Datei speichern",
      "",
      f"{selected_format} Files (*.{selected_format.lower()});;All Files (*)",
  )
  if file_name:
    window.statusBar().showMessage(
        f"Daten gespeichert unter: {file_name}", 3000
    )


def datei_importieren():
  file_name, _ = QFileDialog.getOpenFileName(
      window, "Daten importieren", "", "Alle Unterstützten (*.csv *.json *.xml)"
  )
  if file_name:
    window.statusBar().showMessage(f"Daten importiert aus: {file_name}", 3000)


def datei_exportieren():
  selected_format = format_combo.currentText()
  file_name, _ = QFileDialog.getSaveFileName(
      window,
      "Daten exportieren",
      "",
      f"{selected_format} Files (*.{selected_format.lower()});;All Files (*)",
  )
  if file_name:
    window.statusBar().showMessage(f"Daten exportiert als: {file_name}", 3000)


def oeffne_einstellungen():
  QMessageBox.information(
      window,
      "Einstellungen",
      "Hier kannst du später App-Einstellungen konfigurieren.",
  )


#=========================================================================
btn_speichern.clicked.connect(daten_speichern)
btn_neu.clicked.connect(neues_formular)
btn_loeschen.clicked.connect(daten_loeschen)

# Toolbar Buttons
btn_open.clicked.connect(datei_oeffnen)
btn_save.clicked.connect(datei_speichern_dialog)
btn_import.clicked.connect(datei_importieren)
btn_export.clicked.connect(datei_exportieren)
btn_settings.clicked.connect(oeffne_einstellungen)

#===========================================================================
window.statusBar().showMessage("Bereit. Datensätze geladen")

window.setCentralWidget(central_widget)
window.show()
app.exec()