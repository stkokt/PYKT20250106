"""
Aufgabe: Bibliotheksverwaltungssystem
Erstelle ein einfaches Bibliotheksverwaltungssystem, das die folgenden Klassen umfasst:

Buch:

Attribute: titel, autor, isbn, verfügbar (Boolean)
Methoden:
__init__: Initialisiert ein Buch mit Titel, Autor, ISBN und Verfügbarkeit.
ausleihen: Setzt das Buch als nicht verfügbar.
zurückgeben: Setzt das Buch als verfügbar.
__str__: Gibt eine lesbare Darstellung des Buchs zurück.
Bibliothek:

Attribute: name, bücher (Liste von Buch-Objekten)
Methoden:
__init__: Initialisiert die Bibliothek mit einem Namen und einer leeren Liste von Büchern.
buch_hinzufügen: Fügt ein Buch zur Bibliothek hinzu.
buch_ausleihen: Leiht ein Buch aus, wenn es verfügbar ist.
buch_zurückgeben: Gibt ein Buch zurück.
verfügbare_bücher: Gibt eine Liste der verfügbaren Bücher zurück.
__str__: Gibt eine lesbare Darstellung der Bibliothek und ihrer Bücher zurück.
Benutzer:

Attribute: name, ausgeliehene_bücher (Liste von Buch-Objekten)
Methoden:
__init__: Initialisiert einen Benutzer mit einem Namen und einer leeren Liste von ausgeliehenen Büchern.
buch_ausleihen: Leiht ein Buch aus der Bibliothek aus und fügt es zur Liste der ausgeliehenen Bücher hinzu.
buch_zurückgeben: Gibt ein Buch an die Bibliothek zurück und entfernt es aus der Liste der ausgeliehenen Bücher.
__str__: Gibt eine lesbare Darstellung des Benutzers und seiner ausgeliehenen Bücher zurück.
Beispiel-Workflow:
Erstelle eine Bibliothek.
Füge mehrere Bücher zur Bibliothek hinzu.
Erstelle einen Benutzer.
Der Benutzer leiht ein Buch aus der Bibliothek aus.
Der Benutzer gibt das Buch zurück.
Zeige die verfügbaren Bücher in der Bibliothek an.


Beispiele von Büchern:

1.  Titel: "Der kleine Prinz"

    Autor: Antoine de Saint-Exupéry
    ISBN: 978-3-551-35060-8

2.  Titel: "1984"

    Autor: George Orwell
    ISBN: 978-3-499-22721-5

3.  Titel: "Der Hobbit"

    Autor: J.R.R. Tolkien
    ISBN: 978-3-608-93522-7

4.  Titel: "Die unendliche Geschichte"

    Autor: Michael Ende
    ISBN: 978-3-499-20890-0

5.  Titel: "Harry Potter und der Stein der Weisen"

    Autor: J.K. Rowling
    ISBN: 978-3-551-55167-7

"""

class Medien():
    cnt_media = 0
    def __init__(self, Titel):
        self.titel = Titel
        self.jahr = 0
        self.verfügbar = True

class Buch(Medien):
    cnt_book = 0
    def __init__(self, Titel,ISBN, Autor):
        super().__init__(Titel)
        self.isbn = ISBN
        self.autor = Autor
        self.kategorie = "book"
           
class CD(Medien):
    cnt_cd = 0
    def __init__(self, EAN, Autor):
        self.ean = EAN
        self.autor = Autor
        self.kategorie = "CD"
        
class Nutzer():
    def __init__(self,NutzerID, Name):
        self.id = NutzerID
        self.name = Name
        self.leihliste = []

class Bibliothek():
    def __init__(self, bst=[]):
        self.bestandsliste = bst
        self.nutzerliste = []

    def verleihen(self,nutzer:Nutzer):
        media_idx = 0
        for index, media in enumerate([media for media in self.bestandsliste if media.verfügbar == True]):
            print(index + 1,":  ",media.titel,";", media.autor)
        print()
        media_idx = int(input("Geben Sie den Index des Mediums ein, welches Sie leihen wollen."))
        nutzer.leihliste.append(self.bestandsliste[media_idx-1])
        self.bestandsliste[media_idx-1].verfügbar = False
    
    def ruecknahme(self, nutzer:Nutzer):
        media_idx = 0
        print("Buch zurück")

    def bestandPlus(self,media):
        self.bestandsliste.append(media)

    def bestandAnzeige(self, nutzer):
        action = True
        print("Guten Tag!\nWas wollen Sie tun?\nBuch ausleihen = 1\tBuch zurückgeben = 2")
        action = input("Ihre Eingabe: ")
        if action == "1" or action == "2":
            action = int(action)-1
            if action:
                self.ruecknahme(nutzer)
            else:
                self.verleihen(nutzer)
        else:
            print("Ihre Eingabe war nicht korrekt. Bitte wiederholen Sie.")
            self.bestandAnzeige(nutzer)
        

# Programmablauf


nutzer = []
for idx in range(5):
    nutzer.append(Nutzer(idx, f"Nutzer_{idx}"))

for ntz in nutzer:
    print(ntz.id, ntz.name)

buecher = [Buch("Der kleine Prinz","978-3-551-35060-8", "Antoine de Saint-Exupéry"),
           Buch("1984","978-3-499-22721-5","George Orwell"),
           Buch("Der Hobbit","978-3-608-93522-7","J.R.R. Tolkien"),
           Buch("Die unendliche Geschichte","978-3-499-20890-0","Michael Ende"),
           Buch("Harry Potter und der Stein der Weisen","978-3-551-55167-7","J.K. Rowling")]

for book in buecher:
    print(book.titel,";", book.autor,";", book.isbn)

bib = Bibliothek(buecher)

bib.bestandAnzeige(nutzer[0])

for media in bib.bestandsliste:
    print(media.titel, media.verfügbar)

for media in nutzer[0].leihliste:
    print(nutzer[0].name," Leihliste: ",media.titel,";", media.autor,";", media.isbn)

bib.bestandAnzeige(nutzer[0])