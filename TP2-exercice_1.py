"""
Exercice 1 :
Ecrivez une fonction couleur qui prend en entrée un entier naturel N et retourne
la chaîne de caractères :
 “rouge” si N est un nombre pair strictement plus grand que 10,
 “vert” si N est un nombre impair inférieur ou égal à 25,
 “bleu” sinon
"""


def couleur (n):
    if (n%2==0 and n>=10):
        print("rouge")
    elif(n%2!=0 and n<=25):
        print("vert")
    else:
        print("bleu")

x=int(input("Entrer un nombre entier :"))
couleur(x)
    

    
