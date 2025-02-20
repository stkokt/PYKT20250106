"""
Um eine SQLite-Datenbank zu erstellen, Tabellen zu füllen 
und Änderungen anzuzeigen, können wir die sqlite3-Bibliothek 
in Python verwenden. 
Hier ist ein Beispielcode, der diese Aufgaben erledigt:
"""

import sqlite3

# Verbindung zur SQLite-Datenbank herstellen (oder erstellen, falls sie nicht existiert)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Tabelle 1 erstellen und mit Werten füllen
cursor.execute('''
CREATE TABLE IF NOT EXISTS table1 (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
''')

# Daten in Tabelle 1 einfügen
cursor.execute('INSERT INTO table1 (name, age) VALUES ("Alice", 30)')
cursor.execute('INSERT INTO table1 (name, age) VALUES ("Bob", 25)')

# Tabelle 2 erstellen und mit Werten füllen
cursor.execute('''
CREATE TABLE IF NOT EXISTS table2 (
    id INTEGER PRIMARY KEY,
    product TEXT NOT NULL,
    price REAL
)
''')

# Daten in Tabelle 2 einfügen
cursor.execute('INSERT INTO table2 (product, price) VALUES ("Laptop", 999.99)')
cursor.execute('INSERT INTO table2 (product, price) VALUES ("Smartphone", 499.99)')

# Tabelle 3 erstellen und mit Werten füllen
cursor.execute('''
CREATE TABLE IF NOT EXISTS table3 (
    id INTEGER PRIMARY KEY,
    city TEXT NOT NULL,
    population INTEGER
)
''')

# Daten in Tabelle 3 einfügen
cursor.execute('INSERT INTO table3 (city, population) VALUES ("Berlin", 3769000)')
cursor.execute('INSERT INTO table3 (city, population) VALUES ("Hamburg", 1841000)')

# Änderungen speichern
conn.commit()

# Daten aus den Tabellen auslesen
def read_table(table_name):
    cursor.execute(f'SELECT * FROM {table_name}')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

print("Tabelle 1:")
read_table('table1')

print("\nTabelle 2:")
read_table('table2')

print("\nTabelle 3:")
read_table('table3')

# Änderungen in den Tabellen anzeigen
print("\nÄnderungen in Tabelle 1:")
cursor.execute('UPDATE table1 SET age = 31 WHERE name = "Alice"')
read_table('table1')

# Verbindung schließen
conn.close()
