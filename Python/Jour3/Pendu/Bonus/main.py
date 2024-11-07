import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Importer Pillow

# Fonction principale du jeu
def game():
    global solution, lettres_trouvees, tentatives, affichage
    choix = ["malenia", "milicent", "ranni", "fia", "melina", "hyetta", "sellen", "tanith", "rya", "roderika", "nepheli", "irina", "latenna", "leda", "freyja", "trina"]
    solution = random.choice(choix)
    lettres_trouvees = ""
    tentatives = 7
    affichage = "_ " * len(solution)
    update_affichage()

# Fonction pour mettre à jour l'affichage des lettres trouvées
def update_affichage():
    global affichage_label
    affichage_label.config(text="Pnj féminin à deviner : " + affichage)

# Fonction qui gère la soumission de la lettre par l'utilisateur
def proposer_lettre():
    global solution, lettres_trouvees, tentatives, affichage
    proposition = input_entry.get().lower()
    input_entry.delete(0, tk.END)  # Effacer le champ de saisie après soumission

    # Vérifier que l'utilisateur propose bien une seule lettre
    if len(proposition) != 1 or not proposition.isalpha():
        messagebox.showwarning("Erreur", "Proposez une seule lettre !")
        return

    # Vérification si la lettre a déjà été proposée
    if proposition in lettres_trouvees:
        messagebox.showwarning("Erreur", "Vous avez déjà proposé cette lettre.")
        return

    if proposition in solution:
        lettres_trouvees += proposition
        result_label.config(text="-> Bien vu!")
    else:
        tentatives -= 1
        result_label.config(text=f"-> Nope. Il vous reste {tentatives} tentatives")

    # Mettre à jour l'affichage des lettres trouvées
    affichage = ""
    for x in solution:
        if x in lettres_trouvees:
            affichage += x + " "
        else:
            affichage += "_ "

    update_affichage()

    # Vérifier si le joueur a gagné
    if "_" not in affichage:
        result_label.config(text="     >>> Gagné! <<<      ")
        messagebox.showinfo("Victoire", "Tu as trouvé, c'était bien : " + solution)
        rejouer()

    # Si plus de tentatives, la partie est finie
    if tentatives == 0:
        result_label.config(text="    >>> Défaite! <<<     ")
        messagebox.showinfo("Défaite", "Dommage, la solution était : " + solution)
        rejouer()

# Fonction pour relancer une partie
def rejouer():
    game()

# Interface Tkinter
app = tk.Tk()
app.title("Elden Ring - Pendu")

# Charger et afficher l'image
try:
    # Remplace 'image.png' par le nom de ton fichier image
    image = Image.open("C:/Users/Pc Portable/Documents/molengeek selection/Python/Pendu/Bonus/eldenRing.webp")
    image = image.resize((300, 200), Image.Resampling.LANCZOS)  # Ajuster la taille selon besoin
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(app, image=photo)
    image_label.image = photo  # Garder une référence pour éviter le garbage collection
    image_label.pack(pady=10)
except Exception as e:
    print("Erreur lors du chargement de l'image :", e)

# Champ pour entrer une lettre
input_label = tk.Label(app, text="Proposez une lettre :")
input_label.pack()

input_entry = tk.Entry(app)
input_entry.pack()

proposer_button = tk.Button(app, text="Proposer", command=proposer_lettre)
proposer_button.pack(pady=5)

# Zone pour afficher l'avancement du mot
affichage_label = tk.Label(app, text="Pnj féminin à deviner :")
affichage_label.pack(pady=10)

# Résultat de la tentative
result_label = tk.Label(app, text="")
result_label.pack()

# Lancer une première partie
game()

app.mainloop()
