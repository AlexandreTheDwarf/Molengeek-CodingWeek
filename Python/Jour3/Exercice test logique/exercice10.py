def anagramme (chaine1, chaine2):
    chaine1 = chaine1.lower()
    chaine2 = chaine2.lower()

    lettre1 = ([x for x in chaine1])
    lettre2 = ([x for x in chaine2])

    lettre1.sort()
    lettre2.sort()

    if lettre1==lettre2:
        print (True)
    else :
        print (False)

anagramme("listen", "silent")
anagramme("hello","world")
anagramme("Niche", "chien")