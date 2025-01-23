# Aufgabe 1:
# Nutze die pop-Methode, um die Eingangsliste in die Ausgangsliste umzuformen:

eingangsliste = [68, 44, 52, 92, 11, 4, 61, 69, 67, 3]
ausgangsliste = [52, 4, 61, 67, 3]
print(ausgangsliste.index(61))
liste=[]
liste.insert(0, ausgangsliste.pop(ausgangsliste.index(61)))
print(liste, ausgangsliste)

# Füge hier eine Reihe von pop-Methodenaufrufen ein:
# eingangsliste.pop(...)
# eingangsliste.pop(...)
# ...

# Anfang Lösung

# Musterlösung

# eingangsliste.pop(0)
# eingangsliste.pop(0)
# eingangsliste.pop(1)
# eingangsliste.pop(1)
# eingangsliste.pop(3)



# Alternative 1 mit Loop
# Diese ist relativ "teuer", da der for- Loop jedesmal von vorn beginnt,
# solange die Eingangsliste länger ist als die Ausgangsliste.
# while len(eingangsliste) != len(ausgangsliste):
#     for num in eingangsliste:
#         if num not in ausgangsliste:
#             eingangsliste.pop(eingangsliste.index(num))

# Alternative 2 mit Loop
# Diese ist "günstiger" als Alternative 1, da sowohl der erste for- Loop 
# als auch der zweite jeweils nur einmal ausgeführt wird.

idx = []    # Liste für Indizes, an denen nicht enthaltene Nummern gefunden wurden
for index, num in enumerate(eingangsliste):
    if num not in ausgangsliste:
        idx.append(index)   # Fügt den Index der Indexliste hinzu.

# Das ist im Grunde Stanislavs Lösung. Wir kehren die Liste um,
# um die Eingangsliste von hinten zu verkürzen. Dadurch müssen wir 
# die Indizes nicht verschieben/ neu berechnen.
idx.reverse()

print(idx)

for i in idx:
    eingangsliste.pop(i) # Jetzt schmeißen wir die Elemente von hinten aus der Eingangsliste.

# Es gibt sicherlich noch weitere Schleifenlösungen...

# Ende Lösung

print(f"Eingangsliste: {eingangsliste}")
print(f"Ausgangsliste: {ausgangsliste}")

if eingangsliste == ausgangsliste:
    print("Listen sind identisch! Geschafft!")
else:
    print("Noch entspricht die Eingangsliste nicht der Ausgangsliste")


# Aufgabe 2:
# Nutze die insert-Methode, um die Eingangsliste in die Ausgangsliste umzuformen:

eingangsliste = [52, 4, 61, 67, 3]
ausgangsliste = [68, 44, 52, 92, 11, 4, 61, 69, 67, 3]

# Füge hier eine Reihe von pop-Methodenaufrufen ein:
# eingangsliste.insert(0, 68)
# eingangsliste.insert(index, wer0)
# ...

# Anfang Lösung

# Musterlösung
# eingangsliste.insert(0, 68)
# eingangsliste.insert(1, 44)
# eingangsliste.insert(3, 92)
# eingangsliste.insert(4, 11)
# eingangsliste.insert(7, 69)

# Alternative 1 mit Loop.
for index, num in enumerate(ausgangsliste): # enumerate führt zu [[0,'a'], [1,'b'], [2,'c']]
    if eingangsliste[index] != num:
        eingangsliste.insert(index, num)


# Ende Lösung

print(f"Eingangsliste: {eingangsliste}")
print(f"Ausgangsliste: {ausgangsliste}")

if eingangsliste == ausgangsliste:
    print("Listen sind identisch! Geschafft!")
else:
    print("Noch entspricht die Eingangsliste nicht der Ausgangsliste")



# Aufgabe 3:
# Ersetze Elemente der Eingangsliste mittels Zuweisungsoperator (=), bis die Eingangsliste der Ausgangsliste gleicht:

eingangsliste = [68, 30, 52, 92, 54, 4, 61,  9, 67, 1]
ausgangsliste = [68, 44, 52, 92, 11, 4, 61, 69, 67, 3]

# Füge hier eine Reihe von Zuweisungsoperationen ein:
# eingangsliste[1] = 44
# eingangsliste[index] = wert
# ...

# Anfang Lösung

# Musterlösung
# eingangsliste[1] = 44
# eingangsliste[4] = 11
# eingangsliste[7] = 69
# eingangsliste[9] = 3



# Alternative 1 mit Loop.
for index, num in enumerate(eingangsliste):
    if num != ausgangsliste[index]:
        eingangsliste[index] = ausgangsliste[index]

# Ende Lösung

print(f"Eingangsliste: {eingangsliste}")
print(f"Ausgangsliste: {ausgangsliste}")

if eingangsliste == ausgangsliste:
    print("Listen sind identisch! Geschafft!")
else:
    print("Noch entspricht die Eingangsliste nicht der Ausgangsliste")


# Aufgabe 4:
# Nutze die pop-Methode und insert-Methode um die Eingangsliste in die Ausgangsliste umzuformen:
# Verwende so wenig wie mögliche Methodenaufrufe.

eingangsliste = [68, 52, 92, 60, 54, 4, 50, 9, 67]
ausgangsliste = [68, 30, 52, 92, 54, 4, 61, 67, 1]

# Füge hier eine Reihe von pop- und/oder insert-Methodenaufrunfen ein:
# eingangsliste.insert(index, wert)
# eingangsliste.pop(index)
# ...

# Anfang Lösung

# Musterlösung
eingangsliste.insert(1,30)
eingangsliste.pop(4)
eingangsliste.pop(6)
eingangsliste.insert(6,61)
eingangsliste.pop(7)
eingangsliste.insert(8,1)


# Ende Lösung

print(f"Eingangsliste: {eingangsliste}")
print(f"Ausgangsliste: {ausgangsliste}")

if eingangsliste == ausgangsliste:
    print("Listen sind identisch! Geschafft!")
else:
    print("Noch entspricht die Eingangsliste nicht der Ausgangsliste")



# Aufgabe 5:
# Listen können ebenso wie Strings konkatiniert werden:
#beispiel_liste1 = [1,2,3]
#beispiel_liste2 = [4,5,6]
#beispiel_zusammengesetzte = beispiel_liste1 + beispiel_liste2
#beispiel_zusammengesetzte == [1,2,3,4,5,6]
#print(zusammengesetzte_liste)

liste1 = [68, 30, 52]
liste2 = [60,  4, 61]
liste3 = [40, 92, 54]
liste4 = [61, 67,  1]

ausgangsliste = [68, 30, 52, 92, 54, 4, 61, 67, 1]

# Konkatiniere die Listen in der richtigen Reihenfolge zu einer Eingangsliste und entferne alle störenden Elemente mittels der pop-Methode, bis die Eingangsliste der Ausgangsliste gleicht:
# Füge hier die Operationen ein:
# eingangsliste = liste1_4 + liste1_4 + ... + liste1_4
# eingangsliste.pop(index)
# ...

# Anfang Lösung

# Konkatination muss sein, egal welche Schritte danach kommen.
eingangsliste = liste1 + liste3 + liste2 + liste4

# Musterlösung
# eingangsliste.pop(3)
# eingangsliste.pop(5)
# eingangsliste.pop(6)

# Alternative mit Loop:
for index, num in enumerate(eingangsliste):
    if num != ausgangsliste[index]:
        eingangsliste.pop(index)

# Ende Lösung

print(f"Eingangsliste: {eingangsliste}")
print(f"Ausgangsliste: {ausgangsliste}")

if eingangsliste == ausgangsliste:
    print("Listen sind identisch! Geschafft!")
else:
    print("Noch entspricht die Eingangsliste nicht der Ausgangsliste")


