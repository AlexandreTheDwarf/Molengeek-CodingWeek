(print ("Quelle est ton nom ?"))

nom = input ()

if nom == "Alice" or nom == "Bob" :
    print ("Comment va " + nom + " ?")
else :
    print ("Comment allez vous " + nom + " ?")

# Soluce

nom = input ("Quelle est ton nom ?")
nom.lower()

if nom == "alice" or nom == "bob" :
    print ("Comment va " + nom + " ?")
else :
    print ("Comment allez vous " + nom + " ?")