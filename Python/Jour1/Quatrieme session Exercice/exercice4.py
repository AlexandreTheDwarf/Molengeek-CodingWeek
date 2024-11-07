employés = ["jean", "stephane", "hamid", "christine", "marie"]

# si tu veux inclure hamid :

for employé in employés :
    print (employé)
    if employé == "hamid":
        break
    print (employé)

# si on veux pas inclure hamid :

for employé in employés :
    if employé == "hamid":
        break
    print (employé)