# Das Konzept von mutable/ immutable bedeutet,
# dass es veränderbare und nicht veränderbare Datentypen gibt. 

# Mutable sind Listen, Sets und Dictionaries (LSD)
# Alle anderen Datentypen sind immutable (mit Ausnahme der eigenen durch
# Klassen definierten Datentypen.)
 
# Um das Konzept über die Ausgabe sichtbar zu machen,
# benutzen wir die Builtin Funktion id(), die die Nummer der
# Arbeitsspeicher- Adresse zurückgibt, an der der Wert einer Variablen liegt.

a = 5       # Zahlen sind grundsätzlich immutable.
print("a=5",",Speicheradresse:",hex(id(a))) # Die Speicheradresse wird als Hexadezimalzahl ausgegeben.

print()

# Der Wert der Variable a wird neu zugewiesen.
# Dadurch wird (weil Zahlen immutable) ein neues Objekt 
# mit einer anderen Adresse im Arbeitsspeicher angelegt.

a = 6       
print("a=6",",Speicheradresse:",hex(id(a))) 

print()

# Pythons Speicherkonzept ist so, dass im Speicher Werte, die im Code
# irgendwann mal definiert wurden, vorgehalten werden. Nimmt eine weitere
# Variable diesen Wert an, zeigt sie ebenfalls auf diese Speicheradresse.
# Das ist sehr speichereffizient.

b = 6
print("b=6",",Speicheradresse:",hex(id(b))) # Vergleiche mit Speicheradresse von a!

print()

# Auch bei Sequenzvariablen und deren Elementen ist das so.

char = "e"  # Das Zeichen 'e' wird im Speicher abgelegt.

string_a = "text"   # Die Zeichenkette string_a wird im Speicher abgelegt.
print("string_a = 'text'",",Speicheradresse:",hex(id(string_a)))

print()

string_a = "texte"  # Wegen Veränderung neues Objekt (neue Adresse) im Speicher.
print("string_a = 'texte'",",Speicheradresse:",hex(id(string_a)))

print()

# Aber achte auf die Adressen der Elemente:
# Gleichwertige Elemente = selbe Speicheradresse

for char in string_a:
    print(f"{char}: ","Speicheradresse: ", hex(id(char)))

print()

liste = [1,2,3,4,5,6]
print("'liste'","Speicheradresse vor Änderung: ",hex(id(liste)))

print()

# Neuzuweisung eines einzelnen Elements der Liste;
# dennoch selbe Speicheradresse der Variable 'liste'.

liste[0] = 10
print("'liste'","Speicheradresse nach Änderung: ",hex(id(liste)))

print()

# Beachte, dass die Variable 'liste' in einem ganz anderen 
# Speicherbereich liegt, als deren Elemente.
# Die Elemente können durchaus fragmentiert im Speicher liegen, 
# weil 'liste' die Adressen ihrer kennt.

for num in liste:
   print(f"Listenelement: {num} ","Speicheradresse: ", hex(id(num)))

print()

# Wann kommt das Mutability- Konzept zum Tragen (und kann problematisch werden)?

c = 10

# Variable 'd' hat durch folgende Zuweisung ebenfalls den Wert 10.

d = c

# Ändert man allerdings den Wert von 'c', bleibt der Wert von 'd' dennoch
# bei 10, weil sich für 'd' die Speicheradresse nicht ändert.

c = 11
print("Wert von c:", c, "Adresse von c:", hex(id(c)))
print("Wert von d:", d, "Adresse von d:", hex(id(d)))

print()

# LISTEN

# Der 'liste2' wird der Wert der 'liste1' (also deren Speicherbereich)
# zugewiesen.

liste1 = [1,2,3]
liste2 = liste1

print("'liste1' ","Speicheradresse: ",hex(id(liste1)))
print("'liste2' ","Speicheradresse: ",hex(id(liste2)))

print()

# Ein einzelnes Element der 'liste1' wird verändert.
# Diese Änderung passiert auch in 'liste1'.

liste1[0] = 10
print("'liste1' ","Speicheradresse: ",hex(id(liste1)))
print("'liste2' ","Speicheradresse: ",hex(id(liste2)))

print()

# Weist man allerdings der 'liste1' komplett einen neuen Wert zu,
# wird die Änderung von 'liste2' nicht übernommen, weil sich die Speicheradresse
# von 'liste1' zwar ändert, aber nicht der von 'liste2'.

liste1 = [4,5,6]
print("'liste2' ",liste2)

print()

# Will man eine eigenständige Kopie der 'liste1' der 'liste2'
# zuweisen, nutzt man dfür die Methode copy().

liste2 = liste1.copy()
print("'liste2' ",liste2)   # 'liste2' enthält nun die gleichen Elemente,

print()

# aber beide Listen haben nun verschiedene Speicheradressen

print("'liste1' ",liste1)
print("Adresse von 'liste1':",hex(id(liste1)))
print()
print("'liste2' ",liste2)
print("Adresse von 'liste2':",hex(id(liste2)))

print()

# Nach partieller Änderung der 'liste1'
# ist 'liste2' unverändert.

liste1[0] = 20
print("'liste1' ",liste1)
print("'liste2' ",liste2)

print()

# LOOPS

# Abbruchbedingung!!!!
# break, continue

n = 10

# Gefährliche Schreibweise! Besser: while n>0
# Wenn n == 0, wertet 'while n' zu False aus, und 
# die Schleife bricht ab.
# Wichtig ist, dass innerhalb der Schleife 'n'
# entsprechend verändert wird (decrement), sonst Endlosschleife !!

while n: 
    print(n, end=" ")
    n -= 1

print()

# Das Keyword 'break' bricht die Schleife komplett ab.

n = 10
while n:
    if n==5:
        break
    print(n, end=" ")
    n -= 1

print()

# Das Keyword 'continue' bricht den aktuellen Schleifendurchlauf ab
# und führt den nächsten durch. 

n = 10
while n:
    if n==5:
        n -= 1
        continue
    print(n, end=" ")
    n -= 1

print()
# break und continue funktionieren natürlich auch in for- Loops

# Range- based Loop loopt über die Spannweite einer Sequenz.
for num in liste:
    print(num, end=" ")

print()

# Zählerbasierter Loop loopt n- mal.
""" z.B. in C++

for(int i = 0; i < 10; i++){
    std::cout << i <<std::endl;
}
"""
# Python Syntax für zählerbasierte Loops

# Ausgabe: Zahlen 0 bis 9

for i in range(10):     # range(stop bevor)
    print(i, end=" ")

print()

# Ausgabe: Zahlen 1 bis 10

for i in range(1,11):     # range(start, stop bevor)
    print(i, end=" ")

print()

# Ausgabe: Jede 2. Zahl zwischen 1 und 10

for i in range(1,11,2):     # range(start, stop bevor, step)
    print(i, end=" ")

print()

# Der Stern- Operator entfernt die eckigen Klammern um eine Liste,
# er entpackt diese.

print("Entpackte Liste: ", *liste2)



