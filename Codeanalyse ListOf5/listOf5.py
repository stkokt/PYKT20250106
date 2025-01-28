liste_0_100 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,100]
liste_of_5_a = []
liste_of_5_b = []

tmp_list = []
for num in liste_0_100:
    if num % 5 == 0:
        tmp_list.append(num)
        liste_of_5_a.append(tmp_list)
        liste_of_5_b.append(tmp_list.copy())
    else:
        liste_of_5_a.append(num)
        liste_of_5_b.append(num)

print("liste_of_5_a wurde die tmp_list angehangen.\n")
print(liste_of_5_a)
print("liste_of_5_b wurde eine Kopie der tmp_list angehangen.\n")
print(liste_of_5_b)

print("\nDie Speicheradressen der Listen in liste_of_5_a:\n")
for element in liste_of_5_a:
    if type(element)==list:
        print("Speicheradresse:", hex(id(element)))

print("\nDie Speicheradressen der Listen in liste_of_5_b:\n")
for element in liste_of_5_b:
    if type(element)==list:
        print("Speicheradresse:", hex(id(element)))