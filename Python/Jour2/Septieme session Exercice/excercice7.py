def password(x):
    while x != "admin":
        x = input("Donnez-moi le vrai mot de passe admin ? ")  
        if x != "admin":
            print("Essaye encore")
    print("Bienvenue admin")

password(input("Donnez-moi le mot de passe admin ? ")) 


