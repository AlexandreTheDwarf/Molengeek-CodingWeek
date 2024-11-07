(print ("Donne moi un nombre"))

x = input ()

x = int(x) 

y = x % 2

if x == 0 :
    print (str(x) + " est nul")
elif y == 0 :
    print (str(x) + " est pair")
else :
    print (str(x) + " est impair")

# Soluce

x = int(input("Donnez moi un nombre"))

if x %2 == 0 :
   print (str(x) + " est pair")
elif x == 0 :
    print (str(x) + " est nul")
else :
    print (str(x) + " est impair")
    