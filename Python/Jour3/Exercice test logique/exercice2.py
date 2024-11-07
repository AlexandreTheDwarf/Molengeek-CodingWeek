# Function trouver sur le net car j'avoue que factorielle ça date un peu et j'étais pas trés attentif a ce chapitre en math :(

def factorielle(n):
    if n == 0:
        return 1
    else:
        return n  * factorielle(n-1)


print(factorielle(5))

print(factorielle(0))

print(factorielle(3))