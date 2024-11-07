print ("Donne moi un nombre")

x = input ()
x = int(x) 

print ("Donne moi un autre nombre")

y = input ()
y = int(y) 

print ("Donne moi l'opérateur que tu veux utiliser ? (+,-,*,/)")

op = input ()

if op == "+" :
    print (x+y)
elif op == "/" and y != 0 :
    print (x/y)
elif op == "-" :
    print (x-y)
elif op == "*" :
    print (x*y)
else :
    print ("L'opération est impossible ou tu ne m'as donné le bon opérateur ou tu ne m'as pas donné des chiffres")