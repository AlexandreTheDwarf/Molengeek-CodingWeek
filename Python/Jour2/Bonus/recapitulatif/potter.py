# Exercice 3 : L’énigme de l’escalier infini de poudlard

# Enoncé :
# Tu te retrouves face à un escalier infini qui mene a la chambre des secrets de poudlard avec des marches numérotées. Chaque marche impaire est piégée, mais tu peux poser le pied sur les marches paires. Ton but est d'atteindre la marche numéro n sans jamais poser le pied sur une marche impaire.

# Instructions : 
# Crée une fonction atteindre_sommet(n) qui prend en paramètre un nombre entier n, correspondant au nombre de marches. Utilise une boucle pour afficher toutes les marches que tu peux franchir (les marches paires) jusqu’à atteindre n. Si tu tombes sur une marche impaire, le programme affiche : "Attention, marche piégée !", sinon il affiche "Marche sûre : numéro X".

def atteindre_sommet(n):
    for i in range(n):
        if i%2!=0 :
            print ("Attention, marche piégée !")
        else:
            print ("Marche sûre : numéro " + str(i))
    print ("bravo tu es arivé a la chambre des secrets")

atteindre_sommet (int(input("Combien de marche ce dresse devant toi ?")))