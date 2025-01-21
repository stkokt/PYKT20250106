# Das Konzept von mutable/ immutable bedeutet,
# dass es veränderbare und nicht veränderbare Datentypen gibt. 

# Mutable sind Listen, Sets und Dictionaries (LSD)
# Alle anderen Datentypen sind immutable (mit Ausnahme der eigenen durch
# Klassen definierten Datentypen.)
 
# Um das Konzept über die Ausgabe sichtbar zu machen,
# benutzen wir die Builtin Funktion id(), die die Nummer der
# Arbeitsspeicher- Adresse zurückgibt, an der der Wert einer Variablen liegt.

a = 5       # Zahlen sind grundsätzlich immutable.
print("a=5",hex(id(a))) # Die Speicheradresse wird als Hexadezimalzahl ausgegeben.

# Der Wert der Variable a wird neu zugewiesen.
# Dadurch wird (weil Zahlen immutable) ein neues Objekt 
# mit einer anderen Adresse im Arbeitsspeicher angelegt.

a = 6       
print("a=6",hex(id(a))) 

# Pythons Speicherkonzept ist so, dass im Speicher Werte, die im Code
# irgendwann mal definiert wurden, vorgehalten werden. Nimmt eine weitere
# Variable diesen Wert an, zeigt sie ebenfalls auf diese Speicheradresse.
# Das ist sehr speichereffizient.

b = 6
print("b=6",hex(id(b))) # Vergleiche mit Speicheradresse von a!

# Auch bei Sequenzvariablen und deren Elementen ist das so.

char = "e"  # Das Zeichen 'e' wird im Speicher abgelegt.

string_a = "text"   # Die Zeichenkette string_a wird im Speicher abgelegt.
print(hex(id(string_a)))

string_a = "texte"  # Wegen Veränderung neues Objekt (neue Adresse) im Speicher.
print(hex(id(string_a)))

# Aber achte auf die Adressen der Elemente:

for char in string_a:
    print(hex(id(char)))

liste = [1,2,3,4,5,6]
# print(hex(id(liste)))

liste[0] = 10
#print(hex(id(liste)))

# for num in liste:
#   print(hex(id(num)))

#print(hex(id(string_a)))

#for char in string_a:
#    print(hex(id(char)))

c = 10
d = c

c = 11
# print(c)
# print(d)


liste1 = [1,2,3]
liste2 = liste1.copy()
# print(liste2)

# print(hex(id(liste1)))
# print(hex(id(liste2)))

liste1[0] = 10
# print(liste1)
# print(liste2)
#print(hex(id(liste1)))

liste1 = [4,5,6]
#print(hex(id(liste1)))
#print(liste2)


# Abbruchbedingung
# break, continue

# n = 10
# while n:
#     if n==5:
#         n -= 1
#         continue
#     print(n)
#     n -= 1

liste = [1,2,3]

# for num in liste:
#     print(num)

"""
for(int i = 0; i < 10; i++){
    print(i)
}
"""
# for i in range(1,11):     # range(start, stop bevor, step)
#     print(i)

index = 2

liste2 = [2,5,6]
var = liste2.pop(0)
# print(liste2)
# print(var)
#print(liste[index])

print(*liste2)



