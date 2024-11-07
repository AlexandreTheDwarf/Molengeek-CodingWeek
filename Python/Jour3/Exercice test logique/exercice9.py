def rotate(liste, k):
    liststart = liste[k + 1:]  # À partir de l'élément après k
    listend = liste[:k + 1]  # Inclut l'élément à l'indice k
    result = liststart + listend  # Concatène les deux listes
    print(result)

liste = [1, 2, 3, 4, 5]
rotate(liste, 2)
# [4, 5, 1, 2, 3]

liste = [10,20,30,40,50]
rotate(liste, 3)
# [50, 10, 20, 30, 40]
