# Mutable sind Listen, Sets und Dictionaries
# LSD

a = 5

#print("a=5",hex(id(a)))

a = 6

#print("a=6",hex(id(a)))

b = 6

#print("b=6",hex(id(b)))

char = "e"

string_a = "text"
# print(hex(id(string_a)))

string_a = "texte"
# print(hex(id(string_a)))

liste = [1,2,3,4,5,6]
# print(hex(id(liste)))

liste[0] = 10
#print(hex(id(liste)))

# for num in liste:
#   print(hex(id(num)))

#print(hex(id(string_a)))

#for char in string_a:
#    print(hex(id(char)))

c = 10
d = c

c = 11
# print(c)
# print(d)


liste1 = [1,2,3]
liste2 = liste1.copy()
# print(liste2)

# print(hex(id(liste1)))
# print(hex(id(liste2)))

liste1[0] = 10
# print(liste1)
# print(liste2)
#print(hex(id(liste1)))

liste1 = [4,5,6]
#print(hex(id(liste1)))
#print(liste2)


# Abbruchbedingung
# break, continue

# n = 10
# while n:
#     if n==5:
#         n -= 1
#         continue
#     print(n)
#     n -= 1

liste = [1,2,3]

# for num in liste:
#     print(num)

"""
for(int i = 0; i < 10; i++){
    print(i)
}
"""
# for i in range(1,11):     # range(start, stop bevor, step)
#     print(i)

index = 2

liste2 = [2,5,6]
var = liste2.pop(0)
# print(liste2)
# print(var)
#print(liste[index])

print(*liste2)



