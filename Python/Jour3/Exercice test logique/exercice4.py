# slicing python "x[start:stop:step]"
# :: = start au début et finit a la fin
# step = -1 parcours la chaîne de droite à gauche, donc on inverse l'ordre des caractères.

def palaindrome (x):
    result = x[::-1] 
    if result == x:
        print (True)
    else :
        print (False)

palaindrome ("radar")

palaindrome ("hello")

palaindrome ("level")