fruits = ["pomme", "poire", "peche"]
electro = ["micro-onde", "frigo"]
menages = ["javel", "shampoing", "dentifrice", "eponge"]

course = input("Quelle liste veux tu ? (Fruits, Electro, menages)")
course = course.lower ()

if course == "fruits":
    # printing the list using loop
    for x in range(len(fruits)):
        print (fruits[x]),
elif course == "electro":
    # printing the list using loop
    for x in range(len(electro)):
        print (electro[x]),
elif course == "menages":
    # printing the list using loop
    for x in range(len(menages)):
        print (menages[x]),
else :
    print ("tu ne dois pas acheter ça !")

    