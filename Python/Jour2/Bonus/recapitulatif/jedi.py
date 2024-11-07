# Exercice 1 : Le test du Jedi

# Enoncé :
# Tu es un Jedi en quête d'aventure, et pour entrer dans un temple sur Corusand , tu dois prouver ta sagesse. Le garde te demande de résoudre une énigme : déterminer si on est "de lumière" ou "du coté obscure". Les nombres pairs appartiennent à la lumière, tandis que les nombres impairs appartiennent aux cotés obscurs.

# Instructions : 
# Crée une fonction test_jedi(nombre) qui prend un nombre en paramètre. Si le nombre est pair, retourne "La force est grande en toi", sinon, retourne "Le coté obscur est puissant". Ensuite, demande à l'utilisateur d'entrer un nombre et dis-lui s'il est digne d'entrer dans le temple.

def test_jedi (x):
    if x==0:
        print("Telle est la Voie")
    elif x%2==0 :
        print("La force est grande en toi")
    else :
        print("Le coté obscur est puissant")

test_jedi (int(input("Quelle est ton matricule ?")))