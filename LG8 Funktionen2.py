# Funktionen2 Aufgaben

# Aufgabe 1: Schreibe eine Funktion zur Kreisberechnung, die zwei Argumente übernimmt: einen Zahlenwert
#            und einen String, der aussagt, ob dieser Zahlenwert als Radius, Durchmesser, Umfang oder Fläche zu verstehen ist.
#            Radius soll dabei als Defaultwert eingestellt sein. Die Funktion soll dann die jeweils restlichen 
#            Werte ausgeben.

print("\nAufgabe 1\n")

# Alternative 1
# def kreis(val:int|float, mod:str="r")->None:    # Argument "mod" ist per default mit "r" für Radius belegt
#     '''
#     mod bezeichnet, welchen Wert die übergebene 
#     Variable darstellt
#     Radius="r"      Durchmesser="d"
#     Fläche="a"      Umfang="u"
#     '''
#     from math import pi, sqrt   # Import der Mathebibliothek für PI und Wurzelziehen

#     match mod:  # die verschiedenen Berechnungen in Abhängigkeit vom Modus
#         case "r":
#             d=2*val
#             a=pi*val**2
#             u=pi*2*val
#             print(f"Durchmesser: {round(d, 2)}, Flaeche: {round(a, 2)}, Umfang: {round(u, 2)}")
#         case "d":
#             r=val/2
#             a=(pi*val**2)/4
#             u=pi*val
#             print(f"Radius: {round(r, 2)}, Flaeche: {round(a, 2)}, Umfang: {round(u, 2)}")
#         case "a":
#             r=sqrt(val/pi)
#             d=2*r
#             u=pi*2*r
#             print(f"Radius: {round(r, 2)}, Durchmesser: {round(d, 2)}, Umfang: {round(u, 2)}")
#         case "u":
#             r=val/(2*pi)
#             d=2*r
#             a=pi*r**2
#             print(f"Radius: {round(r, 2)}, Durchmesser: {round(d, 2)}, Flaeche: {round(a, 2)}")

# Alternative 2
# warum nicht einfach nur immer erst den Radius berechnen
# und am Schluss alle anderen Werte:
def kreis(val, mod="r"):
    from math import pi, sqrt
    r=0
    match mod:
        case "r":
            r = val
        case "d":
            r=val/2
        case "u":
            r = val/(2*pi)
        case "a":
            r = sqrt(val/pi)
    d = 2 * r
    u = 2 * pi * r
    a = pi * r**2
    print(f"Radius: {round(r,2)}\nDurchmesser: {round(d,2)}\nUmfang: {round(u,2)}\nFläche: {round(a,2)}\n")

kreis(5)
kreis(5,"d")
kreis(5,"a")
kreis(5,"u")



# Aufgabe 2: Schreibe eine Funktion, die einen String (z.B. "c", "t", "r" für Circle, Triangle, Rectangle)
#            und eine Argumentenliste (*args) von Floats als Argumente übernimmt.
#            In der Funktion sollen weitere Funktionen definiert sein, die je nach 
#            Anforderung den Flächeninhalt eines Kreises, rechtwinkligen Dreiecks oder
#            Rechtecks zurückgeben. Als Werte bei der Dreicksberechnung sollen als Übergabe-
#            parameter die Längen der Seiten angenommen werden, die den rechten Winkel
#            einschließen.

print("\nAufgabe 2\n")

def flaeche(mod, *werte):
    from math import pi
    def circle_a():
        return pi * werte[0]**2       # Kreisfläche
    def rect_a():
        return werte[0]*werte[1]      # Rechteckfläche
    match mod:
        case "c":
            print(f"Der Flächeninhalt des Kreises beträgt {round(circle_a(),2)}.\n")
        case "t":
            print(f"Der Flächeninhalt des Dreieckes beträgt {round(rect_a()/2,2)}.\n")
        case "r":
            print(f"Der Flächeninhalt des Rechteckes beträgt {round(rect_a(),2)}.\n")
# Aufrufe
flaeche("c",5)
flaeche("t",5,2)
flaeche("r",5,2)

# Aufgabe 3: Schreibe eine Funktion, die folgendes Dictionary, eine Argumentenliste (*args)
#            und eine Keywordargumentenliste (**kwargs) übernimmt.
#            Die Funktion soll für alle Namen ausgeben: 
#            z.B. "Hallo Herr Schneider!" bzw. "Hallo Frau Müller!"

namen = {
    "Anna Müller": "w",
    "Laura Schmidt": "w",
    "Max Mustermann": "m",
    "Maria Becker": "w",
    "Sophie Wagner": "w",
    "Paul Meier": "m",
    "Lukas Schneider": "m",
    "Julia Fischer": "w",
    "Felix Weber": "m",
    "Jonas Hoffmann": "m"
}

print("\nAufgabe 3\n")

def hallo(namedict:dict, *geschlecht, **anrede):
    for name, sex in namedict.items():
        if sex == geschlecht[0]:  # Index 0 der Tupels geschlecht
            print(f"Hallo {list(anrede.values())[0]} {name.split()[-1]}!")
        if sex == geschlecht[1]:  # Index 1 der Tupels geschlecht
            print(f"Hallo {list(anrede.values())[1]} {name.split()[-1]}!")
    # die Values des Dictionarys am Index 1 gesplittet und davon das letzte Element
# Aufruf:
hallo(namen,'m','w',geschlecht1="Herr", geschlecht2="Frau")

# Aufgabe 4: Schreibe zwei Passwortgeneratoren, die ein Passwort aus Groß- und
#            Kleinbuchstaben, Zahlen und Sonderzeichen zurückgeben. 
#            Der erste soll als Argument die Anzahl der Zeichen übernehmen. 
#            Der zweite die Anzahl der Groß- und Kleinbuchstaben, Zahlen und 
#            Sonderzeichen parametrieren können. Tipp: Nutze das Modul "string".
#            https://docs.python.org/3/library/string.html

print("\nAufgabe 4\n")

def pwgenSimple(pwLength:int)->str:
    """
    @param pwLength: Integerzahl für die Anzahl der auszugebenen Zeichen
    @return: Zufällige Zeichenkette
    """
    from string import hexdigits, punctuation
    from random import sample 
    pwPool=hexdigits + punctuation  # Alle Zahlen und Buchstaben und die Sonderzeichen
    # print(pwPool)     # nur einkommentieren, um den Zeichenpool zu sehen
    return "".join(sample(pwPool, pwLength))    # Sampleliste wird in einen leeren String gejoint

print(pwgenSimple(20))

def pwgenPro1(lows:int, caps:int, nums:int, specs:int=0)->str:  
    # siehe ab Zeile 164, sinngemäß gleich, nur hier unter Verwendung des String- Moduls
    from random import sample, shuffle
    from string import ascii_lowercase, ascii_uppercase, digits, punctuation
    lowLetters=sample(ascii_lowercase, lows)
    capLetters=sample(ascii_uppercase, caps)
    numbers=sample(digits, nums)
    specChar=sample(punctuation, specs)
    pw=[]
    pw.extend(lowLetters+capLetters+numbers+specChar)
    shuffle(pw)
    return "".join(pw)

print(pwgenPro1(2,3,4,4))

def pwgenPro2(lows:int, caps:int, nums:int, specs:int=0)->str:
    from random import sample, shuffle
    lowLetters=sample(range(97, 123), lows) # range(97, 123): Kleinbuchstaben im Ascii-Code
    capLetters=sample(range(65, 91), caps)  # range(65, 91): Großbuchstaben im Ascii-Code
    numbers=sample(range(48, 58), nums)     # range(48, 58): Zahlen im Ascii-Code
    specChar=sample(range(35, 39), specs)   # range(35, 39): Einige Soderzeichen im Ascii-Code
    pw=[]                                   # leere Liste angelegt
    pw.extend(lowLetters+capLetters+numbers+specChar)   # und erweitert um die Einzellisten
    pw=[chr(num) for num in pw] # Umwandlung der numerischen Ascii- Entsprechung in Zeichen
    shuffle(pw)                 # Durchmischen
    return "".join(pw)          # und in einen leeren String joinen

print(pwgenPro2(2,3,4,4))

# Aufgabe 5: Schreibe eine Liste von Lambda- Funktionen, die mittels Loops auf 
#            jedes Element der Liste 'zahlen' nacheinander angewandt werden.
#            Lambdas: x+1,  x/2,  x**2
#            Gebe anschließend die Liste 'zahlen' aus.

print("\nAufgabe 5\n")

lambdas = [(lambda x: x+1), (lambda x: x/2), (lambda x: x**2)]
zahlen = [1,2,3,4,5,6]

# Alternative 1
# for i in range(len(zahlen)):
#     for func in lambdas:
#         zahlen[i] = func(zahlen[i])

# Alternative 2
# for func in lambdas:
#     zahlen = list(map(func, zahlen))

# Alternative 3
for func in lambdas:
    zahlen = [func(x) for x in zahlen]

print(zahlen)