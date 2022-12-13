def compte(chaine,char):
    cpt=0
    for i in range(len(chaine)):
        if char==chaine[i]:
            cpt+=1
    return cpt
chaine=input("Enrer un mot :")
char=input("entrer une lettre :")
print("le nombre d'occurences de ",char," dans le mot ",chaine," est :",compte(chaine,char))

def frequence(chaine):
    a=(compte(chaine,'a')/int(len(chaine)))
    b=(compte(chaine,'b')/int(len(chaine)))
    c=(compte(chaine,'c')/int(len(chaine)))
    d=(compte(chaine,'d')/int(len(chaine)))
    L=[a,b,c,d]
    return L
L=[]
print('La fréquence de a,b,c et d dans cette chaine :',frequence(chaine))

