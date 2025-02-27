class Kreis():
    anzahl_kreis = 0
    def __init__(self, d):
        self.durchmesser = d
        Kreis.anzahl_kreis +=1
        self.__name = "Kreis"
    def __str__(self):
        return f"Ich bin ein Kreis mit Durchmesser {self.durchmesser}."
    def __del__(self):
        Kreis.anzahl_kreis -=1
    def __whoami(self):
        return self.__name
    def sayHello(self):
        return f"Hello, I am {self.__whoami()}."

    
r1 = Kreis(5)
print(r1)
r1.__name = "Viereck"
#print(r1.whoami())
print(r1.__name)
#print(r1.__whoami())
print(r1.sayHello())
print("Anzahl Kreise vor delete:",Kreis.anzahl_kreis)
del(r1)
print("Anzahl Kreise nach delete:",Kreis.anzahl_kreis)
print()

kreise = []

for i in range(5):
    kreise.append(Kreis(i))

for i in range(5):
    print(kreise[i])

print()
print("Anzahl Kreise in der Liste vor delete:",Kreis.anzahl_kreis)
print()

del(kreise[0])

for i in range(len(kreise)):
    print(kreise[i])

print()
print("Anzahl Kreise in der Liste nach delete:",Kreis.anzahl_kreis)