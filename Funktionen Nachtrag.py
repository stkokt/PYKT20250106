# FUNKTIONEN II

# All, Any, Map, Filter, Zip (Alles Builtin Funktionen)

# All, Any
print(all([1,2,0,4,7,8,9])) # False, weil eine Null dabei ist (Nicht alle sind True)
print(any([1,2,0,4,7,8,9])) # True, weil mindestens eine Zahl nicht 0 ist

# Map, Filter
def make_even(x):
    if x%2 != 0:
        return x + 1
    else:
        return x

liste= list(map(make_even,[1,2,0,4,7,8,9]))
print(liste)    # [2, 2, 0, 4, 8, 8, 10]

def is_even(x):
    if x % 2 == 0:
        return x
    
liste= list(filter(is_even,[1,2,0,4,7,8,9]))
print(liste)    # [2, 4, 8]

# Zip

listeA = [1,3,5,7,9]
listeB = [2,4,6,8]
listeC = list(zip(listeA, listeB))

print(listeC)   # [(1, 2), (3, 4), (5, 6), (7, 8)] Die 9 fehlt, weil sie keinen Partner hat.

# Default Parameter

def add(x, y=1):
    return x+y

number = 10

number = add(number)
print(number)   # 11

number = add(number, 8)
print(number)   # 19

# Namensräume

x=5     # globale Variable

def scope():
    x=10 # nichtlokal für Unterfunktionen, lokal scope()
    def glob():
        global x
        print(f"Globale Variable {x}")
    def nonloc():
        nonlocal x        
        print(f"Nichtlokale Variable {x}")
    def loc():
        x=15 # lokal für loc() 
        print(f"Lokale Variable {x}")
    glob()
    nonloc()
    loc()
    
scope()

# Lambda- Funktionen (Kurzfunktionen, anonyme Funktionen)
# z.B. lambda x: x+1 oder lambda x, y: x * y

listeA = [1,3,5,7,9]
listeD = [(lambda x: x+1)(x) for x in listeA] # Addiert 1 zu jedem Listenelement
print(listeD)   # [2, 4, 6, 8, 10]

listeD = [(lambda x, y: x * y)(x, 2) for x in listeD] # Multipliziert jedes Listenelement mit 2
print(listeD)   # [4, 8, 12, 16, 20]

# Args und Kwargs

def aFunction(var, *args, **kwargs):
    '''
    Es muss nicht *args und **kwargs heißen, 
    wichtig sind die Sternchen.
    *args wird als Tupel interpretiert,
    **kwargs als Dictionary.
    '''

    print(type(var))
    print(type(args))
    print(type(kwargs))

    print(f"Das ist die Variable: {var}.")
    print(f"Das ist das Args- Tupel: {args}")
    print(f"Das ist das Kwargs- Dictionary: {kwargs}")
    for value in kwargs.values():
        print(args[0]*value)

aFunction("Var", 5,"m",3.14, kwargs1 = "Hallo", kwargs2 = "Welt")

