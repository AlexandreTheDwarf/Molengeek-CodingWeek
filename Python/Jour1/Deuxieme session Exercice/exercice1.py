print ("Donne moi un nombre")

x = input ()

x = int(x) 

if x > 0 :
    print (str(x)+ " est positif")
elif x < 0 :
    print (str(x) + " est négatif")
else :
    print (str(x) + " est nul")

# Soluce :

x = int(input("Donnez moi un nombre"))

if x > 0 :
    print (str(x)+ " est positif")
elif x < 0 :
    print (str(x) + " est négatif")
else :
    print (str(x) + " est nul")
