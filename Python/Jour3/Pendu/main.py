import random

def game():
    choix = ["malenia", "milicent", "ranni", "fia", "melina", "hyetta", "sellen", "tanith", "rya", "roderika", "nepheli", "irina", "latenna", "leda", "freyja", "trina"]
    solution = random.choice(choix)

    tentatives = 7
    lettres_trouvees = ""

    # Initialiser l'affichage
    affichage = "_ " * len(solution)  # On crée une chaîne avec des underscores pour chaque lettre

    while tentatives > 0:
        print("Pnj féminin de Elden Ring à deviner : ", affichage)
        proposition = input("Proposez une lettre : ").lower()  # On convertit la proposition en minuscule
        
        # Vérification pour n'accepter qu'une seule lettre
        while len(proposition) != 1 or not proposition.isalpha():  
            proposition = input("Proposez une seule lettre : ").lower()  
        
        # Vérification si la lettre a déjà été proposée
        if proposition in lettres_trouvees:
            print("Vous avez déjà proposé cette lettre.")
            continue  # On passe à l'itération suivante de la boucle

        if proposition in solution:
            lettres_trouvees += proposition  # Ajouter la lettre trouvée
            print("-> Bien vu!")
        else:
            tentatives -= 1  # Décrémente le nombre de tentatives
            print("-> Nope. Il vous reste", tentatives, "tentatives")

        # Mettre à jour l'affichage
        affichage = ""  # Réinitialiser affichage pour la mise à jour
        for x in solution:
            if x in lettres_trouvees:
                affichage += x + " "  # Afficher la lettre trouvée
            else:
                affichage += "_ "  # Afficher un underscore pour les lettres non trouvées

        # Vérifier si le joueur a gagné
        if "_" not in affichage:
            print("     >>> Gagné! <<<      ")
            print("tu as trouvé c'était bien: " + affichage)
            break

    print("    * Fin de la partie *    ")



def play_games():
    # Play repeatedly.
    while True:  # Loop forever.
       game()  # Play one game.
       answer = input("Veux tu rejouer? O/N ").upper()
       if answer == 'N':
           break

play_games()

# print ("⠉⢻⡟⠉⠉⠇⠤⣤⠄⠀⠠⣤⡤⣤⣀⠀⢤⣤⠤⣤⠤⣤⡤⠀⠠⣤⠄⠀⠀⢤⡤⢤⣀⠀⢤⣤⠤⠤⣤⠄⠀⠠⣤⢄⣴⠖⠋⠉⢲")
# print ("⠀⢸⣇⣀⣠⠀⠀⣿⠀⠀⠀⢸⠀⠀⠘⣷⡀⣿⣀⡌⠀⢸⠻⣦⡀⢸⠀⠀⠀⢸⣇⣠⡿⠀⠀⣿⠀⠀⣿⠻⣄⠀⡇⣾⡏⠀⠀⠀⠈⠀")
# print ("⠀⢸⡇⠀⠈⠀⠀⣿⠀⠀⡤⣸⡀⠀⢠⡿⢀⣿⠀⢁⡄⢸⠀⠈⠻⣾⠀⠀⠀⢸⡏⠻⣦⠀⠀⣿⠀⠀⣿⠀⠙⢷⡇⢹⣷⠀⠀⠉⣿⡏")
# print ("⠀⠾⠷⠤⢤⠾⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠉⠉⠉⠉⠈⠉⠉⠀⠀⠉⠀⠀⠀⠉⠉⠀⠈⠉⠉⠉⠉⠉⠉⠉⠀⠀⠉⠀⠙⠳⠦⠤⠿")