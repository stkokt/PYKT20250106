# Mehrfachvererbung

class Haus:
    def __init__(self, h, b, t):
        self.hoehe = h
        self.breite = b
        self.tiefe = t
        self.__vol = 0

class Fahrzeug:
    def __init__(self, cnt_r):
        self.anz_raeder = cnt_r

class Wohnmobil(Haus, Fahrzeug):
    def __init__(self, h, b, t, r):
        Haus.__init__(self, h, b, t)
        Fahrzeug.__init__(self, r)

    def __str__(self):
        return f"Ich bin {self.hoehe}m hoch, {self.breite}m breit, {self.tiefe}m tief und habe {self.anz_raeder} Räder."

# Beispiel zur Verwendung
wohnmobil = Wohnmobil(3, 2.5, 6, 4)
print(wohnmobil)

