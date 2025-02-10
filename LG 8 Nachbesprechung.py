# LG 8 Nachbesprechung

# Da die prints im Folgendem teils sehr umfangreich sind,
# sind sie erstmal auskommentiert. Kommentiert sie euch jeweils
# wieder ein, wenn ihr sie in der Ausgabe sehen wollt.

# Frage 1: Wie kann ich sehen, welche Module auf dem Rechner
# bereits installiert sind?

# print(help('modules'))

# Frage 2: Wie kann ich mir die Hilfe zu einem bestimmten
# Modul anzeigen lassen?

# print(help('math'))   # beispielsweise das Mathemodul

# Frage 3: Wie kann ich mir die Hilfe zu einer bestimmten
# Methode eines bestimmten Moduls anzeigen lassen?

# print(help('math.sqrt'))   # Mathemodul -> Quadratwurzel

# Frage 4: Wie kann ich mir die Methoden eines bestimmten 
# Moduls anzeigen lassen ohne die komplette Dokumentation?

# Importieren des Moduls und dann mit der dir()- Funktion

import math
# print(dir(math))

# Frage 5: Wie kann ich Module nachinstallieren bzw. updaten?
# https://pip.pypa.io/en/stable/
# Konsole öffnen und eingeben:
# pip install -m <modulname> bzw.
# pip install --upgrade <modulname>

# Frage 6: Wie kann ich eine randomisiert Zahlenliste in Zeichen
# umwandeln? (benutzt in LG8 Funktionen2 Zeile 172) 

from random import sample

rand_zahlen = sample(range(65,91),5)
# rand_zahlen enthält nun 5 zufällige Zahlen von 65 bis 90

# print(rand_zahlen)

# Der Bereich deckt sich in der ASCII Tabelle mit der numerischen
# Ensprechung der Großbuchstaben. 
# siehe: https://www.doeben-henisch.de/fh/I-THINF/TH-THINF/VL5/ascii-lenz.htm
# Aber wie kann ich die Zahlen in der Liste rand_zahlen nun in 
# Buchstaben umwandeln? -> Builtin Funktion chr()

rand_grossbuchstaben = [chr(num) for num in rand_zahlen]

# print(rand_grossbuchstaben)

# Frage 7: Kann ich Ranges kombinieren?
# Ja, z.B. so:

sonderzeichen = list(range(40, 48)) + list(range(58, 65)) + list(range(91, 97))
rand_sonderzeichen = sample(sonderzeichen, 5)   # 5 ASCII - Codes für Sonerzeichen
# print(rand_sonderzeichen)

# Umwandlung in tatsächliche Zeichen
rand_sonderzeichen = [chr(sz) for sz in rand_sonderzeichen]
# print(rand_sonderzeichen)

# Frage 8: Kann man bestimmte Sonderzeichen nachträglich ausschließen?
# Ja, z.B. als Differenzmenge:

sonderzeichen = set(sonderzeichen) - {92, 41, 40}
# print(sonderzeichen)

# Frage 9: Wie kann ich Duplikate aus Listen entfernen?
# Methode 1: Umwandlung in ein Set. Da es das Wesensmerkmal eines Sets ist,
#            jedes Element nur einmal zu enthalten, wird dabei jedes Duplikat
#            entfernt. Eventueller Nachteil: Die Elemente werden geordnet.

liste = [1,2,4,3,6,1,5,2,2]
liste = set(liste)
print(liste)

# Methode 2: Nutze die fromkeys- Methode des Datentypy Dicionary.
#            Dadurch bleibt die Reihenfolge erhalten.

liste2 = [1,2,4,3,6,1,5,2,2]
liste2 = list(dict().fromkeys(liste2))
print(liste2)

