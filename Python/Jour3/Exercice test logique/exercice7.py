# fonction qui teste si un nombre est un carré parfait ou non trouver sur le net mais modifier pour pouvoir rajouter start et end
# https://www.tresfacile.net/solution-exercise-28-algorithme-qui-determine-la-liste-des-carres-parfait/

# fonction qui test si un nombre est carré parfait ou non
def testCarreParfait(n):
    # initialisation compteur count 
    count = 0
    
    for i in range(1, n + 1):
        if i * i == n:
            count += 1
    return count > 0  # Retourne True si count > 0, sinon False

# fonction qui détermine la liste des carrés parfaits     
def listCarresParfait(start, end):
    # initialisation de la liste des carrés parfaits
    lparfait = []
    for i in range(start, end + 1):  # Utilise les paramètres de plage
        if testCarreParfait(i):
            lparfait.append(i)
    return lparfait
 
# Tests :
print(listCarresParfait(1, 30))
# [1, 4, 9, 16, 25]
print(listCarresParfait(10, 50))
# [16, 25, 36, 49]
print(listCarresParfait(5, 10))
# [9]