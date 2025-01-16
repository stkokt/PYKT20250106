# Aufgaben zu den Themen Strings, Listen und Verzweigungen


# Listen

# 1. Gebe das erste und das letzte Element der folgenden Liste aus.

liste_A = [2,4,7,5,3,9,11,15,12]

print("\nAufgabe 1\n")

print(f"Erstes Element: {liste_A[0]}, letztes Element: {liste_A[8]}")
print(f"Erstes Element: {liste_A[0]}, letztes Element: {liste_A[-1]}")
print(f"Erstes Element: {liste_A[0]}, letztes Element: {liste_A[len(liste_A)-1]}")

# 2. Gebe aus der folgenden Liste die 5 aus:

liste_B = [1,2,3,4,5,6,7,8,9]

print("\nAufgabe 2\n")

print(liste_B[4])
print(liste_B[(len(liste_B)//2)])

# 3. Gebe die Summe der Elemente aus liste_A aus. 
# Nutze dazu die Builtin- Funktion sum().

print("\nAufgabe 3\n")

print(sum(liste_A))


# 4. Gebe den Durchschnittswert aller Elemente aus liste_A aus:
# Nutze dazu die Builtin- Funktionen sum() und len().

print("\nAufgabe 4\n")

print(sum(liste_A)/len(liste_A))


# 5. Gebe das größte Element der folgenden Liste aus. 
# Nutze dazu die Builtin- Funktion max().

liste_C = [9, 29, 68, 8, 80, 6, 93, 172, 17, 137, 166, 1, 162, 67, 10, 48, 129, 125, 128, 109, 7, 126, 51, 157, 28]

print("\nAufgabe 5\n")

print(f"Das größte Element der Liste C ist: {max(liste_C)}")


# 6. Gebe aus, ob das größte Element der liste_C gerade oder ungerade ist.

print("\nAufgabe 6\n")

if (max(liste_C)%2==0):
    print("Das größte Element der Liste C ist gerade.")
else:
    print("Das größte Element der Liste C ist ungerade.")



# 7. Um wieviele Elemente ist liste_C größer als die Summe der Elemente von liste_A und liste_B?

print("\nAufgabe 7\n")

print(f"Die Liste C ist um {len(liste_C)-len(liste_A + liste_B)} Elemente größer als die Summe der Elemente von Liste A und Liste B")



# 8. Ist das kleinste Element der liste_C kleiner als das größte aller Elemente von liste_A und liste_B?
# Wenn ja, wie groß ist der Unterschied?

print("\nAufgabe 8\n")

if min(liste_C) < max(liste_A + liste_B):
    print(f"Das kleinste Element der Liste C ist kleiner als das größte aller Elemente von liste_A und liste_B. \
          Der Unterschied beträgt {max(liste_A + liste_B) - min(liste_C)}")
else:
    print(f"Das kleinste Element der Liste C ist größer als das größte aller Elemente von liste_A und liste_B.")


# 9. Vertausche das erste und das letzte Element von liste_A.

# Variante 1: Klassischer Tauschalgorithmus

print("\nAufgabe 9\n")

swap = liste_A[0]
liste_A[0] = liste_A[-1]
liste_A[-1] = swap

print(liste_A)

# Variante 2: Python- Weg (pythonic)

liste_A[0], liste_A[-1] = liste_A[-1], liste_A[0]

print(liste_A)

# 10. Gebe aus der folgenden Liste das 'y' vom 'Python' aus.

liste_D = ["Ich", "lerne", "Python."]

print("\nAufgabe 10\n")

print(liste_D[2][1])


# BONUS FÜR DIE FORTGESCHRITTENEN (Es werden Schleifen und ggf. Methoden des Datentyps 'str' benötigt)

# 11. Enthält liste_C mehr gerade oder mehr ungerade Zahlen?
# Erhöhter Schwierigkeitsgrad: Nutze dazu nur eine Zählvariable.

print("\nAufgabe 11\n")

# Variante 1 mit zwei Zählvariablen.

gerade = 0
ungerade = 0

for num in liste_C:
    if num % 2 == 0:
        gerade += 1
    else:
        ungerade += 1

if gerade > ungerade:
    print("Liste C enthält mehr gerade Zahlen als ungerade.")
elif gerade == ungerade:
    print("Liste C enthält genauso viele gerade Zahlen wie ungerade.")
else:
    print("Liste C enthält mehr ungerade Zahlen als gerade.")


# Variante 2 mit nur einer Zählvariablen.

gerade_ungerade = 0

for num in liste_C:
    if num % 2 == 0:
        gerade_ungerade += 1
    else:
        gerade_ungerade -= 1

if gerade_ungerade > 0:
    print("Liste C enthält mehr gerade Zahlen als ungerade.")
elif gerade_ungerade == 0:
    print("Liste C enthält genauso viele gerade Zahlen wie ungerade.")
else:
    print("Liste C enthält mehr ungerade Zahlen als gerade.")


# 12. Zähle die Vokale und Umlaute im string.

vokale = ['a', 'e', 'i', 'o', 'u']
umlaute = ['ä', 'ö', 'ü']

string = "Es grünt so grün, wenn Spaniens Blüten blühen. Ich glaub, jetzt hat sie's"

print("\nAufgabe 12\n")

cnt_vokale = 0
cnt_umlaute = 0

for letter in string:
    if letter.lower() in vokale:
        cnt_vokale += 1
    if letter.lower() in umlaute:
        cnt_umlaute += 1

print(f"Der String enthält {cnt_vokale} Vokale und {cnt_umlaute} Umlaute.")


# 13. Verändere den String so, dass jedes Wort mit einem Großbuchstaben beginnt.

print("\nAufgabe 13\n")

string = string.title()

print(string)

# 14. Mache aus dem String eine Liste von Wörtern des Strings.

print("\nAufgabe 14\n")

string = string.split(" ")


print(string)


# 15. Zähle die Worte, die mit einem 'G' beginnen.

print("\nAufgabe 15\n")

startswith_G = 0
for wort in string:
    if wort.startswith('G'):
        startswith_G += 1

print(f"{startswith_G} Worte des Strings beginnnen mit 'G'.")



