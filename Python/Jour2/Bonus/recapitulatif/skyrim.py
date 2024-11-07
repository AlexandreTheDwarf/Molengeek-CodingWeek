#Exercice 4 : Le Tuum du Dovakin

# Enoncé :
# Les dragons anciens ont laissé un message codé sous forme de chiffres (Tuum). Ton objectif est de déchiffrer ce code. Le message est un nombre, et tu dois appliquer la règle suivante : pour chaque chiffre du nombre, si le chiffre est pair, tu le multiplies par 2, et si le chiffre est impair, tu le remplaces par 0. Ensuite, tu devras afficher le message déchiffré, une fois fait, crée un message donnant le pouvoir en fonction.

# Instructions : 
# Crée une fonction dechiffrer_code(code) qui prend un nombre (code) en paramètre, puis utilise une boucle pour traiter chaque chiffre. Affiche le code final déchiffré.

def dechiffrer_code(code):
    # Convertir le nombre en chaîne de caractères pour traiter chaque chiffre
    code_str = str(code)
    
    # Créer une liste pour stocker le résultat déchiffré
    resultat = []
    
    # Boucle pour traiter chaque chiffre
    for chiffre in code_str:
        chiffre = int(chiffre)  # Convertir chaque caractère en entier
        if chiffre % 2 != 0:  # Si le chiffre est impair
            resultat.append(0)  # On remplace par 0
        else:
            resultat.append(chiffre * 2)  # Si pair, on le multiplie par 2
    
    # Afficher le message déchiffré
    print("Message déchiffré :", resultat)
    
    match resultat:
        case [x, *_] if 0 <= x <= 5:  # Si le premier élément est entre 0 et 5
            print("Pouvoir activé : Fus Roh Dah")
        case [x, *_] if 6 <= x <= 9:  # Si le premier élément est entre 6 et 9
            print("Pouvoir activé : Yol Toor Shul")
        case _:
            print("Pas de pouvoir activé")

# Exemple d'appel de la fonction
dechiffrer_code(5123)

dechiffrer_code(28932)

dechiffrer_code(45986)
