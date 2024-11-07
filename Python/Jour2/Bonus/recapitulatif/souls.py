# Exercice 2 : Le mimic

# Enoncé :
# Tu as découvert un coffre a Anor Londo, mais attention, certains coffre sont des mimic et peuvent te couter des HP! Trouve un moyen de faire un pile ou face , si c'est pile , tu tue le mimic mais si c'est face , il t'attaque.

# Instructions : 
# Crée une fonction calculer_points(liste_pieces) qui prend une liste de pièces (nombres entiers) et retourne le total des points gagnés. Chaque pièce d'or (pile) ajoute +10 points et chaque pièce piégée (face) enlève -5 points. Utilise une boucle pour parcourir la liste.

import random

def calculer_points(liste_pieces):
    hp = 100
    for i in range(liste_pieces):
        piece=random.randint(1,2)
        if piece == 1:
            print("pile")
            hp = hp+10
        if piece == 2:
            print("face")
            hp = hp-5
            if hp <=0:
              print("You Are Dead")
              break  
    print("HP restant :" + str(hp))

calculer_points(int(input("Combien lances tu de piece ?")))