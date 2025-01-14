# 1. Setze das Rindvieh PAP in Code um.

"""
janein=input("Funktioniert die Anlage? j/n\n")

if janein=="j":
    print("Fummel bloß nicht dran rum")
    print("Alles klar!")
else:
    janein=input("Hast du dran rumgespielt? j/n\n")
    if janein=="j":
        print("Du Rindvieh!")
        janein=input("Hat es jemand gemerkt? j/n\n")
        if janein=="j":
            print("Du armes Schwein!")
            janein=input("Kannst du jemandem die Schuld zuschieben? j/n\n")
            if janein=="n":
                print("Du armes Schwein!")
            else:
                print("Alles klar!")
        else:
            print("Pfeiffe unauffällig 'La Paloma' und verschwinde!")
            print("Alles klar!")
    else:
        janein=input("Wird man dich verantwortlich machen? j/n\n")
        if janein=="j":
            print("Du armes Schwein!")
            janein=input("Kannst du jemandem die Schuld zuschieben? j/n\n")
            if janein=="n":
                print("Du armes Schwein!")
            else:
                print("Alles klar!")
        else:
            print("Kümmer dich nicht drum!")
            print("Alles klar!")
"""

# 2. Schreibe einen Algorithmus zum Ermitteln,
#    ob ein Jahr ein Schaltjahr ist.

jahr = int(input("Gebe eine Jahreszahl ein:\n"))

if (jahr % 4 == 0 and not jahr % 100 == 0) or (jahr % 400 == 0):
     print(f"Das Jahr {jahr} ist ein Schaltjahr.")
else:
    print(f"Das Jahr {jahr} ist kein Schaltjahr.")

# 3. Ein Auto soll zwei Eigenschaften haben: Farbe und Marke
#    Ist es ein roter BMW, soll die Ausgabe lauten:
#    "Das ist ein schönes Auto"
#    Ist es ein rotes Auto einer anderen Marke, soll die Ausgabe lauten:
#    "Das ist ein schönes Auto der Marke ..." (die Marke statt der Punkte)
#    Ist es ein BMW mit einer anderen Farbe, soll die Ausgabe lauten:
#    z.B. "Das ist ein blauer BMW."
#    Ist es eine andere Marke mit einer anderen Farbe, soll die Ausgabe lauten:
#    z.B. "Das ist ein blaues Auto der Marke ..." (die Marke statt der Punkte)

autofarbe = input("Gebe die Farbe des Autos ein:\n")
automarke = input("Gebe die Marke des Autos ein:\n")

if autofarbe == "rot" and automarke == "BMW":
    print("Das ist ein schönes Auto!")
elif autofarbe == "rot" and automarke != "BMW":
    print(f"Das ist ein schönes Auto der Marke {automarke}.")
elif autofarbe != "rot" and automarke == "BMW":
    print(f"Das ist ein {autofarbe}er BMW.")
else:
    print(f"Das ist ein {autofarbe}es Auto der Marke {automarke}.")