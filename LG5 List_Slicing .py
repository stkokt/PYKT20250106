# Aufgabe 1: Die folgende Liste enthält 80 Elemente. Nutze List- Slicing, um 
#            a) die erste Hälfte auszugeben.
#            b) die letzten 15 Elemente auszugeben.
#            c) die mittleren 40 Elemente auszugeben.
#            d) die letzte Hälfte rückwärts auszugeben. 

big_list =[41, 19, 21, 7, 18, 26, 25, 28, 24, 14, 
           17, 35, 18, 11, 19, 20, 44, 33, 7, 33, 
           7, 35, 5, 35, 46, 50, 9, 4, 41, 39,
           42, 39, 15, 35, 45, 44, 30, 49, 37, 25,
           2, 41, 1, 5, 12, 39, 23, 20, 28, 21,
           17, 39, 36, 18, 22, 49, 36, 4, 42, 16,
           35, 19, 47, 27, 23, 40, 9, 38, 49, 26,
           4, 29, 10, 43, 15, 12, 45, 47, 25, 34]

print("\nAufgabe 1a\n")
print(big_list[0:40])  # oder big_list[0:len(big_list)//2]
print("\nAufgabe 1b\n")
print(big_list[65:81]) # oder big_list[len(big_list)-15:len(big_list)+1]
print("\nAufgabe 1c\n")
print(big_list[20:61]) # oder big_list[20:len(big_list)-19]
print("\nAufgabe 1d\n")
print(big_list[80:39:-1]) # oder big_list[len(big_list):len(big_list)//2-1:-1]

# Aufgabe 2: Slice und konkatiniere die folgende Liste so,
#            dass sie sortiert ist und gebe sie aus.

liste = [5,4,3,2,1,10,9,8,7,6]

print("\nAufgabe 2\n")

liste_sorted = liste[4::-1] + liste[9:4:-1]
print(liste_sorted)

liste1 = [1,2,3,5,6,7,5,12,64,0,5,96]

# Aufgabe 3a: Slice die Liste1 in einem Loop durch Verschieben
#             des Start- Parameters so, dass die Summe der restlichen
#             Liste kleiner 100 ist. Der Loop soll dann abgebrochen und die 
#             gekürzte Liste ausgegeben werden.

# >            (<150)             <
#  |x ->| | | | | | | | | | |stop|

print("\nAufgabe 3a\n")

for x in range(len(liste1)):
    if sum(liste1[x:])<150:
        print(liste1[x:])
        break

# Aufgabe 3b: Slice die Liste1 in einem Loop durch Verschieben
#             des Stop- Parameters so, dass die Summe der restlichen
#             Liste größer 100 ist. Der Loop soll dann abgebrochen und die 
#             gekürzte Liste ausgegeben werden.

# >            (>100)            <
#  |start| | | | | | | | | | |<-x|

print("\nAufgabe 3b\n")

for x in range(len(liste1)):
    if sum(liste1[0:x])>100:
        print(liste1[0:x])
        break

# Aufgabe 3c: Slice die Liste1 in einem Loop durch Verschieben
#             der Start- und Stop- Parameter so, dass die Summe der restlichen
#             Liste kleiner 100 ist. Der Loop soll dann abgebrochen und die 
#             gekürzte Liste ausgegeben werden.

# >            (<100)           <
#  |x->| | | | | | | | | | |<-x|

print("\nAufgabe 3c\n")

for x in range(len(liste1)):
    if sum(liste1[x:len(liste1)-x])<100:
        print(liste1[x:len(liste1)-x])
        break