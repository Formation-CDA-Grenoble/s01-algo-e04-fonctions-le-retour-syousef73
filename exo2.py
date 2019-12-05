def rankInside(list, element):
    n=-1
    for items in list:
        n=n+1
        if items == element:
           
          return n
        



# Pas touche!
tests = (
    ([1, 2, 3], 2, 1),
    ([1, 2, 3], -1, None),
    (["pomme", "banane", "orange"], "pomme", 0),
    (["pomme", "banane", "orange"], "cerise", None),
)

for test in tests:
    print(f"L'appel  rankInside({test[0]}, {test[1]})  renvoie: {rankInside(test[0], test[1])} (résultat attendu: {test[2]})")
