# FUNKTIONEN

# Aufgabe 1: Schreibe eine Funktion, die einen String
#            für einen Namen als Argument übernimmt und 
#            eine Ausgabe erzeugt 'Hallo' + Name.

print("\nAufgabe 1\n")

def hello(name):
    print(f"Hallo {name}!")

hello("Stefan")

# Aufgabe 2: Schreibe eine Funktion, die einen Münzwurf
#            simuliert und das Ergebnis ausgibt. Nutze dazu 
#            eine geeignete Methode des random- Moduls.

print("\nAufgabe 2\n")

def flipcoin():
    from random import choice
    print(choice(["Kopf", "Zahl"]))

flipcoin()

# Aufgabe 3: Schreibe eine Funktion, die mehrere Münzwurfe
#            simuliert und die Häufigkeit von Kopf und Zahl
#            ausgibt. Nutze dazu eine geeignete Methode des 
#            random- Moduls.

print("\nAufgabe 3\n")

def multiFlipcoin(loops):
    from random import choice
    kopf = 0
    zahl = 0
    for n in range(loops):
        wurf = choice(["Kopf", "Zahl"])
        if wurf == "Kopf":
            kopf += 1
        else:
            zahl += 1
    print(f"Bei {loops} Münzwürfen fiel {kopf} mal Kopf und {zahl} mal Zahl." )

multiFlipcoin(100)

# Aufgabe 4: Schreibe eine Funktion, die zwei Zahlen 
#            als Argumente übernimmt und deren Summe 
#            zurückgibt.

print("\nAufgabe 4\n")

def summe(a,b):
    return a+b

print(summe(10,5))

# Aufgabe 5: Schreibe eine gleichnamige Funktion wie in Aufgabe 3,
#            die drei Zahlen als Argumente übernimmt und deren Summe 
#            zurückgibt. Prüfe ob du diese Funktion noch mit 
#            mit zwei Zahlen aufrufen kannst.

print("\nAufgabe 5\n")

def summe(a,b,c):
    return a+b+c

print(summe(10, 15, 20))
# print(sum(10, 15))

# Aufgabe 6: Schreibe eine Funktion, die eine außerhalb der 
#            Funktion definierte Liste von Zahlen als Argument
#            übernimmt und deren einzelne Elemente um 1 erhöht.

print("\nAufgabe 6\n")

def plusOne(lst):
    for i in range(len(lst)):
        lst[i] += 1

zahlen = [1,2,3,4,5]

plusOne(zahlen)

print(zahlen)

# Aufgabe 7: Schreibe eine Funktion, 
#            die den größten Teiler einer Zahl findet.

print("\nAufgabe 7\n")

def maxDivisor(zahl):
    mdiv = zahl//2
    if type(zahl) != int:
        print("Keine Integerzahl übergeben.")
        return 0
    else:
        while zahl % mdiv != 0:
            mdiv -= 1
        print(f"Größter Teiler ist {mdiv}.")
        return mdiv
    
maxDivisor(1_000_009)

# Aufgabe 8: Schreibe eine Funktion, die aus folgendem
#            Dictionary 'Einkaufsliste' dem Gesamtpreis errechnet.

print("\nAufgabe 8\n")

shoppinglist = {"Zeitung":1, "Kartoffeln":2.5, "Salami":5, "Besen":10}

def sumPrices(shoplst:dict):
    return sum(shoplst.values())

print(sumPrices(shoppinglist))

# Aufgabe 9: Schreibe eine Funktion, die aus folgendem
#            Dictionary 'leute' das Durchschnittsalter errechnet.

print("\nAufgabe 9\n")

leute = {"Kerstin": 50, "Manfred": 65, "Lilly": 25}

def avgAge(crowd:dict):
    return round(sum(crowd.values())/len(crowd),2)

print(avgAge(leute))

# Aufgabe 10: Schreibe eine Funktion, die aus dem Dictionary 'leute'
#            die älteste errechnet.

print("\nAufgabe 10\n")

def oldest(crowd:dict):
    maxKey = ""
    maxVal = 0
    for k,v in crowd.items():
        if v > maxVal:
            maxKey = k
            maxVal = v
    print(f"Die älteste Person ist {maxKey}.")

oldest(leute)

# HARDCORE - LEVEL !!!

# Aufgabe 11: Schreibe die Funktion aus Aufgabe 8 so um,
#            dass sie mehrere Personen ausgeben kann, die
#            alle das höchste Alter haben, aber nur eine 
#            Person, sollte diese die älteste sein.

print("\nAufgabe 11\n")

leute2 = {"Kerstin": 50, "Manfred": 65, "Lilly": 25, "Egon" : 65, "Ida" : 55}

def oldest2(crowd:dict):
    maxKey = []
    maxVal = 0
    for k,v in crowd.items():
        if v > maxVal:
            maxKey.clear()
            maxKey.append(k)
            maxVal = v
        elif v == maxVal:
            maxKey.append(k)
    if len(maxKey) > 1:
        print(f"{("".join(str(maxKey).split()).strip("[]")).replace("'", "")} sind die Ältesten.")
    else:            
        print(f"{maxKey} ist am ältesten.")

oldest2(leute2)

# Aufgabe 12: Schreibe eine Funktion, die aus dem Dictionary 'noten'
#             den Notendurchnitt pro Person und pro Fach
#             errechnet.

print("\nAufgabe 12\n")

noten = {"Benny":{"Bio":2.5, "Mathe":1.8, "Deutsch":3.1},\
         "Anja":{"Bio":1.5, "Mathe":2.9, "Deutsch":2.4},\
         "Hanno":{"Bio":4, "Mathe":3.5, "Deutsch":5}}

def avgGrades(grades:dict):
    for k, v in grades.items():
        print(f"{k} hat einen Notendurchschnitt von {round(sum(v.values())/len(v),1)}")
    tmp_dict = dict()
    for v in grades.values():
        tmp_dict.update(v)
    tmp_list = list(tmp_dict.keys())
    tmp_list2 = [[fach, 0, 0] for fach in tmp_list]
    for v in grades.values():
        for k, v1 in v.items():
            for fach in tmp_list2:
                if k == fach[0]:
                    fach[1] += 1
                    fach[2] += v1
    print()
    for fach in tmp_list2:
        print(f"{fach[0]} hat einen Durchschnitt von {round(fach[2]/fach[1], 2)}")

avgGrades(noten)