"""
Xlwings ist eine Python-Bibliothek, die es ermöglicht, Excel-Dateien über Python zu steuern.
Sie bietet eine einfache Möglichkeit, Excel-Dateien zu lesen, zu schreiben und zu manipulieren,
und kann auch mit Excel-Makros und benutzerdefinierten Funktionen (UDFs) arbeiten. Hier sind 
einige grundlegende Beispiele zur Verwendung von Xlwings:

Installation
Bevor du Xlwings verwenden kannst, musst du es installieren. Du kannst das mit pip tun:


pip install xlwings
"""

import xlwings as xw

# Schreiben in eine Excel-Datei

# Erstelle ein neues Arbeitsbuch
workbook = xw.Book()

# Wähle das aktive Arbeitsblatt aus
sheet = workbook.sheets.active

# Schreibe Daten in eine Zelle
sheet.range('A1').value = 'Hallo, Welt!'

# Speichere die Datei
workbook.save('example.xlsx')

# Schließe die Datei
workbook.app.quit()

# Lesen einer Excel-Datei

# Öffne die Excel-Datei
workbook = xw.Book('example.xlsx')

# Wähle das aktive Arbeitsblatt aus
sheet = workbook.sheets.active

# Lese den Wert einer bestimmten Zelle
cell_value = sheet.range('A1').value
print(cell_value)

# Durchlaufe alle Zellen in einem Bereich
for cell in sheet.range('A1:B2'):
    print(cell.value)

# Schließe die Datei ohne Änderungen zu speichern
workbook.app.quit()


# Arbeiten mit mehreren Arbeitsblättern

# Erstelle ein neues Arbeitsbuch
workbook = xw.Book()

# Erstelle ein neues Arbeitsblatt
sheet = workbook.sheets.add(name='Neues Blatt')

# Schreibe Daten in das neue Arbeitsblatt
sheet.range('A1').value = 'Daten im neuen Blatt'

# Speichere die Datei
workbook.save('example.lsx')

# Schließe die Datei
workbook.app.quit()

# Arbeiten mit Diagrammen

# Erstelle ein neues Arbeitsbuch
workbook = xw.Book()
sheet = workbook.sheets.active

# Schreibe einige Daten
sheet.range('A1').value = [['Kategorie', 'Wert'], ['A', 10], ['B', 20], ['C', 30]]

# Erstelle ein Diagramm
chart = sheet.charts.add()
chart.set_source_data(sheet.range('A1').expand())
chart.chart_type = 'column_clustered'

# Speichere die Datei
workbook.save('example_chart.xlsx')

# Schließe die Datei
workbook.app.quit()

# Verwendung von benutzerdefinierten Funktionen (UDFs)

# Definiere eine benutzerdefinierte Funktion
@xw.func
def hallo(name):
    return f'Hallo, {name}!'

# Speichere die UDF in einer Excel-Datei
workbook = xw.Book()
sheet = workbook.sheets.active

# Verwende die UDF in einer Zelle
sheet.range('A1').formula = '=hallo("Welt")'

# Speichere die Datei
workbook.save('example_udf.xlsx')

# Schließe die Datei
workbook.app.quit()

# MAKROS IN EXCEL

def fuellen_bereich():
    # Öffne die Excel-Datei oder erstelle eine neue
    workbook = xw.Book('example.xlsm')
    sheet = workbook.sheets.active

    # Fülle den Bereich A1:D3 mit Werten
    values = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    sheet.range('A1:D3').value = values

    # Speichere die Datei
    workbook.save()

    # Schließe die Datei nicht, da du sie weiterhin verwenden möchtest
    # workbook.app.quit()

# Verknüpfe die Funktion mit einem Button in Excel
@xw.func
def run_makro():
    fuellen_bereich()

"""
Schritt 3: Verknüpfe die Funktion mit einem Button in Excel

Öffne die Excel-Datei (example.xlsm).
Gehe zum Arbeitsblatt, auf dem du den Button platzieren möchtest.
Füge einen Button ein:
Gehe zum Reiter "Entwicklertools" (falls nicht sichtbar, aktiviere 
es in den Excel-Optionen).
Klicke auf "Einfügen" und wähle "Button (Formularsteuerelement)" aus.
Zeichne den Button auf das Arbeitsblatt.
Weise dem Button die Makro-Funktion zu:
Nachdem du den Button gezeichnet hast, wird ein Dialogfeld angezeigt, 
in dem du das Makro auswählen kannst.
Wähle run_makro aus der Liste aus.

Schritt 4: Führe das Makro aus

Klicke auf den Button in Excel, um das Makro auszuführen und den
Bereich A1:D3 mit den Werten zu füllen.
"""