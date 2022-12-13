def polynome(n):
    res=n*(4*n**2 -1)/3
    return res
n=int(input("1-Entrer un nombre entier :"))
print("le resultat est :",polynome(n))

def sci(n):
    res=0
    for i in range(1,n+1):
        res=res+((2*i-1)**2)
    return res
print("le resultat est :",sci(n))

def test_formule(n):
    res=False
    if (polynome(n)==sci(n)):
        res=True
    return res

print(test_formule(n))
        
