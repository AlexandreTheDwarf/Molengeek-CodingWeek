# Crée deux dictionnaires contenant des informations sur des étudiants 1 avec les clés : "nom", "age", et "moyenne" et l'autre avec les clés "classe" et "année". Utilisez une méthode pour fusionner les deux dictionanires en un seul.

eleve = {
    "nom" : ["Marie", "Pierre", "Kévin"],
    "age" : [13, 15, 17],
    "moyenne" : [12.5, 16.0, 17.5]
}

local = {
    "classe" : ["A", "B", "C"],
    "année" : [1, 3, 5]
}

eleve.update(local)

print (eleve)

