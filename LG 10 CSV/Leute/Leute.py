import csv

# Beispiel CSV-Daten
csv_data = """Name,Alter,Stadt
Alice,30,Berlin
Bob,25,Hamburg
Charlie,35,München"""

# CSV-Daten in eine Datei schreiben (für dieses Beispiel)
with open('beispiel.csv', 'w', newline='') as file:
    file.write(csv_data)



# CSV-Datei mit DictReader lesen
with open('beispiel.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    leute = list(reader)
    # next(reader)
    for row in reader:
        print(row)

print(leute)

with open('outputFromDictWriter1.csv', mode='w', newline='') as file:
    # Spaltennamen definieren
    fieldnames = leute[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Kopfzeile schreiben
    writer.writeheader()

    # Daten zeilenweise schreiben
    for row in leute:
        writer.writerow(row)