# crée une fonction de calcul qui prendra trois réponse de l'utilisateur: choisir le premier nombre, choisir l'opérateur, choisir le deuxieme nombre.
# Ensuite, Retournez le résultat du calcul selon l'opérateur mathématique.

def calcul (a,b,c):
    if b == "+" :
        calcul = a + c
        print(calcul)
    elif b == "-" :
        calcul = a - c
        print(calcul)
    elif b == "*":
        calcul = a * c
        print(calcul)
    elif b == "/":
        if c != 0:
            calcul = a / c
            print(calcul)
        else :
            print("division par 0 impossible")
    else :
        print("les instructions donnés ne sont pas correct")

a = int(input("Donne-moi un premier chiffre: "))
b = input("Donne-moi un signe (+,-,/,*): ")
c = int(input("Donne-moi un second chiffre: "))

calcul(a,b,c)