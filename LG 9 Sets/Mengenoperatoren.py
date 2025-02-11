# In Python gibt es mehrere Operatoren, die speziell für Sets verwendet 
# werden können. Diese Operatoren ermöglichen es, verschiedene Mengenoperationen
# durchzuführen. Hier sind die wichtigsten:

#1. Union (`|`): Gibt die Vereinigung zweier Sets zurück, d.h. alle Elemente, 
#   die in mindestens einem der Sets vorhanden sind.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
# union_set ist {1, 2, 3, 4, 5}

# 2. Intersection (`&`): Gibt die Schnittmenge zweier Sets zurück, d.h. alle 
#    Elemente, die in beiden Sets vorhanden sind.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1 & set2
# intersection_set ist {3}

# 3. Difference (`-`): Gibt die Differenz zweier Sets zurück, d.h. alle Elemente,
#    die im ersten Set, aber nicht im zweiten Set vorhanden sind.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1 - set2
# difference_set ist {1, 2}

# 4. Symmetric Difference (`^`): Gibt die symmetrische Differenz zweier Sets zurück,
#    d.h. alle Elemente, die in genau einem der Sets vorhanden sind.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
sym_diff_set = set1 ^ set2
# sym_diff_set ist {1, 2, 4, 5}

# 5. Subset (`<=`): Überprüft, ob ein Set eine Teilmenge eines anderen Sets ist, 
#    d.h. alle Elemente des ersten Sets sind auch im zweiten Set vorhanden.

set1 = {1, 2}
set2 = {1, 2, 3}
is_subset = set1 <= set2
# is_subset ist True

# 6. Proper Subset (`<`): Überprüft, ob ein Set eine echte Teilmenge eines anderen 
#    Sets ist, d.h. alle Elemente des ersten Sets sind auch im zweiten Set vorhanden,
#    und das erste Set ist nicht gleich dem zweiten Set.

set1 = {1, 2}
set2 = {1, 2, 3}
is_proper_subset = set1 < set2
# is_proper_subset ist True


# 7. Superset (`>=`): Überprüft, ob ein Set eine Obermenge eines anderen Sets ist, 
#    d.h. alle Elemente des zweiten Sets sind auch im ersten Set vorhanden.

set1 = {1, 2, 3}
set2 = {1, 2}
is_superset = set1 >= set2
# is_superset ist True

# 8. Proper Superset (`>`): Überprüft, ob ein Set eine echte Obermenge eines 
#    anderen Sets ist, d.h. alle Elemente des zweiten Sets sind auch im ersten 
#    Set vorhanden, und das erste Set ist nicht gleich dem zweiten Set.

set1 = {1, 2, 3}
set2 = {1, 2}
is_proper_superset = set1 > set2
# is_proper_superset ist True

# 9. Equality (`==`): Überprüft, ob zwei Sets gleich sind, d.h. sie enthalten 
#    genau die gleichen Elemente.

set1 = {1, 2, 3}
set2 = {3, 2, 1}
are_equal = set1 == set2
# are_equal ist True

# 10. Inequality (`!=`): Überprüft, ob zwei Sets ungleich sind, d.h. sie enthalten
#     nicht genau die gleichen Elemente.

set1 = {1, 2, 3}
set2 = {4, 5, 6}
are_not_equal = set1 != set2
# are_not_equal ist True




