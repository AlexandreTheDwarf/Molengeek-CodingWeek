# Vous allez crée une solution qui propose (comme un terminal des départs dans une gare) 4 villes accessibles en train.

villes = ["charleroi", "namur", "bruxelles", "anvers"]

# L'utilisateur doit pouvoir choisir pour laquelle des 4 destinations il désire prendre le train. 

print ("Quelle est votre destination ? (charleroi, namur, bruxelles, anvers)")

destination = input ()

charleroiPrix = [5,7,6]
namurPrix = [4,6,5]
bruxellesPrix = [6,8,7]
anversPrix = [7,8,9]

# Lorsque l'utilisateur a choisis sa destination, on lui demande combien de place enfants, combien de places adultes et combien de place senior il souhaite réserver. 

print ("Combien de place enfants avez vous besoin ? ")

billet = []

billet.append(int(input ()))

print ("Combien de place adultes avez vous besoin ? ")

billet.append(int(input ()))

print ("Combien de place seniors avez vous besoin ? ")

billet.append(int(input ()))

print (billet)

# Chaque destination à un prix précis et différent en fonction que l'on soit adulte, enfant ou un senior. Utilisez des conditions pour développer chaque situation.

if destination == villes[0]:
    total = (billet[0] * charleroiPrix[0]) + (billet[1] * charleroiPrix[1]) + (billet[2] * charleroiPrix[2])
    if billet[0] > 0 and billet[1] > 0 and billet[2] > 0 :
        print ("Votre trajet pour " + (destination) + "pour " + str(billet[0]) + " enfant(s) à " + str(charleroiPrix[0]) + " € par personnes et " + str(billet[1]) + " adulte(s) à " + str(charleroiPrix[1]) + " € par personnes et " + str(billet[2]) + " senior(s) à " + str(charleroiPrix[2]) + " € par personnes vous coutera un total de: " + str(total) + " €" )
    elif billet[0] == 0 and billet[1] > 0 and billet[2] > 0 :
        print ("Votre trajet pour " + (destination) + "pour " + str(billet[1]) + " adulte(s) à " + str(charleroiPrix[1]) + " € par personnes et " + str(billet[2]) + " senior(s) à " + str(charleroiPrix[2]) + " € par personnes vous coutera un total de: " + str(total) + " €" )
    elif billet[0] > 0 and billet[1] == 0 and billet[2] > 0 :
        print ("Votre trajet pour " + (destination) + "pour " + str(billet[0]) + " enfant(s) à " + str(charleroiPrix[0]) + " € par personnes et " + str(billet[2]) + " senior(s) à " + str(charleroiPrix[2]) + " € par personnes vous coutera un total de: " + str(total) + " €" )
    elif billet[0] > 0 and billet[1] > 0 and billet[2] == 0 :
              print ("Votre trajet pour " + (destination) + "pour " + str(billet[0]) + " enfant(s) à " + str(charleroiPrix[0]) + " € par personnes et " + str(billet[1]) + " adulte(s) à " + str(charleroiPrix[1]) + " € par personnes vous coutera un total de: " + str(total) + " €" )  
    elif billet[0] > 0 and billet[1] == 0 and billet[2] == 0 :
              print ("Votre trajet pour " + (destination) + "pour " + str(billet[0]) + " enfant(s) à " + str(charleroiPrix[0]) + " € par personnes vous coutera un total de: " + str(total) + " €" )           
    elif billet[0] == 0 and billet[1] > 0 and billet[2] == 0 :
              print ("Votre trajet pour " + (destination) + "pour " + str(billet[1]) + " adulte(s) à " + str(charleroiPrix[1]) + " € par personnes vous coutera un total de: " + str(total) + " €" )           
    else :
              print ("Votre trajet pour " + (destination) + "pour " + str(billet[2]) + " senior(s) à " + str(charleroiPrix[2]) + " € par personnes vous coutera un total de: " + str(total) + " €" )           
elif destination == villes[1] :
    total = (billet[0] * namurPrix[0] ) + (billet[1] * namurPrix[1]) + (billet[2] * namurPrix[2])
    if billet[0] > 0 and billet[1] > 0 and billet[2] > 0 :
        print ("Votre trajet pour " + (destination) + " pour " + str(billet[0]) + " enfant(s) à " + str(namurPrix[0]) + " € par personne et " + str(billet[1]) + " adulte(s) à " + str(namurPrix[1]) + " € par personne et " + str(billet[2]) + " senior(s) à " + str(namurPrix[2]) + " € par personne vous coûtera un total de: " + str(total) + " €" )
    elif billet[0] == 0 and billet[1] > 0 and billet[2] > 0 :
        print ("Votre trajet pour " + (destination) + " pour " + str(billet[1]) + " adulte(s) à " + str(namurPrix[1]) + " € par personne et " + str(billet[2]) + " senior(s) à " + str(namurPrix[2]) + " € par personne vous coûtera un total de: " + str(total) + " €" )
    elif billet[0] > 0 and billet[1] == 0 and billet[2] > 0 :
        print ("Votre trajet pour " + (destination) + " pour " + str(billet[0]) + " enfant(s) à " + str(namurPrix[0]) + " € par personne et " + str(billet[2]) + " senior(s) à " + str(namurPrix[2]) + " € par personne vous coûtera un total de: " + str(total) + " €" )
    elif billet[0] > 0 and billet[1] > 0 and billet[2] == 0 :
        print ("Votre trajet pour " + (destination) + " pour " + str(billet[0]) + " enfant(s) à " + str(namurPrix[0]) + " € par personne et " + str(billet[1]) + " adulte(s) à " + str(namurPrix[1]) + " € par personne vous coûtera un total de: " + str(total) + " €" )  
    elif billet[0] > 0 and billet[1] == 0 and billet[2] == 0 :
        print ("Votre trajet pour " + (destination) + " pour " + str(billet[0]) + " enfant(s) à " + str(namurPrix[0]) + " € par personne vous coûtera un total de: " + str(total) + " €" )           
    elif billet[0] == 0 and billet[1] > 0 and billet[2] == 0 :
        print ("Votre trajet pour " + (destination) + " pour " + str(billet[1]) + " adulte(s) à " + str(namurPrix[1]) + " € par personne vous coûtera un total de: " + str(total) + " €" )           
    else :
        print ("Votre trajet pour " + (destination) + " pour " + str(billet[2]) + " senior(s) à " + str(namurPrix[2]) + " € par personne vous coûtera un total de: " + str(total) + " €" )
elif destination == villes[2] :
    total = (billet[0] * bruxellesPrix[0]) + (billet[1] * bruxellesPrix[1]) + (billet[2] * bruxellesPrix[2])
    if billet[0] > 0 and billet[1] > 0 and billet[2] > 0 :
        print ("Votre trajet pour " + (destination) + " pour " + str(billet[0]) + " enfant(s) à " + str(bruxellesPrix[0]) + " € par personne et " + str(billet[1]) + " adulte(s) à " + str(bruxellesPrix[1]) + " € par personne et " + str(billet[2]) + " senior(s) à " + str(bruxellesPrix[2]) + " € par personne vous coûtera un total de: " + str(total) + " €" )
    elif billet[0] == 0 and billet[1] > 0 and billet[2] > 0 :
        print ("Votre trajet pour " + (destination) + " pour " + str(billet[1]) + " adulte(s) à " + str(bruxellesPrix[1]) + " € par personne et " + str(billet[2]) + " senior(s) à " + str(bruxellesPrix[2]) + " € par personne vous coûtera un total de: " + str(total) + " €" )
    elif billet[0] > 0 and billet[1] == 0 and billet[2] > 0 :
        print ("Votre trajet pour " + (destination) + " pour " + str(billet[0]) + " enfant(s) à " + str(bruxellesPrix[0]) + " € par personne et " + str(billet[2]) + " senior(s) à " + str(bruxellesPrix[2]) + " € par personne vous coûtera un total de: " + str(total) + " €" )
    elif billet[0] > 0 and billet[1] > 0 and billet[2] == 0 :
        print ("Votre trajet pour " + (destination) + " pour " + str(billet[0]) + " enfant(s) à " + str(bruxellesPrix[0]) + " € par personne et " + str(billet[1]) + " adulte(s) à " + str(bruxellesPrix[1]) + " € par personne vous coûtera un total de: " + str(total) + " €" )  
    elif billet[0] > 0 and billet[1] == 0 and billet[2] == 0 :
        print ("Votre trajet pour " + (destination) + " pour " + str(billet[0]) + " enfant(s) à " + str(bruxellesPrix[0]) + " € par personne vous coûtera un total de: " + str(total) + " €" )           
    elif billet[0] == 0 and billet[1] > 0 and billet[2] == 0 :
        print ("Votre trajet pour " + (destination) + " pour " + str(billet[1]) + " adulte(s) à " + str(bruxellesPrix[1]) + " € par personne vous coûtera un total de: " + str(total) + " €" )           
    else :
        print ("Votre trajet pour " + (destination) + " pour " + str(billet[2]) + " senior(s) à " + str(bruxellesPrix[2]) + " € par personne vous coûtera un total de: " + str(total) + " €" )
elif destination == villes[3] :
    total = (billet[0] * anversPrix [0]) + (billet[1] * anversPrix[1]) + (billet[2] * anversPrix[2])
    if billet[0] > 0 and billet[1] > 0 and billet[2] > 0 :
        print ("Votre trajet pour " + (destination) + " pour " + str(billet[0]) + " enfant(s) à " + str(anversPrix[0]) + " € par personne et " + str(billet[1]) + " adulte(s) à " + str(anversPrix[1]) + " € par personne et " + str(billet[2]) + " senior(s) à " + str(anversPrix[2]) + " € par personne vous coûtera un total de: " + str(total) + " €" )
    elif billet[0] == 0 and billet[1] > 0 and billet[2] > 0 :
        print ("Votre trajet pour " + (destination) + " pour " + str(billet[1]) + " adulte(s) à " + str(anversPrix[1]) + " € par personne et " + str(billet[2]) + " senior(s) à " + str(anversPrix[2]) + " € par personne vous coûtera un total de: " + str(total) + " €" )
    elif billet[0] > 0 and billet[1] == 0 and billet[2] > 0 :
        print ("Votre trajet pour " + (destination) + " pour " + str(billet[0]) + " enfant(s) à " + str(anversPrix[0]) + " € par personne et " + str(billet[2]) + " senior(s) à " + str(anversPrix[2]) + " € par personne vous coûtera un total de: " + str(total) + " €" )
    elif billet[0] > 0 and billet[1] > 0 and billet[2] == 0 :
        print ("Votre trajet pour " + (destination) + " pour " + str(billet[0]) + " enfant(s) à " + str(anversPrix[0]) + " € par personne et " + str(billet[1]) + " adulte(s) à " + str(anversPrix[1]) + " € par personne vous coûtera un total de: " + str(total) + " €" )  
    elif billet[0] > 0 and billet[1] == 0 and billet[2] == 0 :
        print ("Votre trajet pour " + (destination) + " pour " + str(billet[0]) + " enfant(s) à " + str(anversPrix[0]) + " € par personne vous coûtera un total de: " + str(total) + " €" )           
    elif billet[0] == 0 and billet[1] > 0 and billet[2] == 0 :
        print ("Votre trajet pour " + (destination) + " pour " + str(billet[1]) + " adulte(s) à " + str(anversPrix[1]) + " € par personne vous coûtera un total de: " + str(total) + " €" )           
    else :
        print ("Votre trajet pour " + (destination) + " pour " + str(billet[2]) + " senior(s) à " + str(anversPrix[2]) + " € par personne vous coûtera un total de: " + str(total) + " €" )
else :
    print ("mauvaise encodage de données")