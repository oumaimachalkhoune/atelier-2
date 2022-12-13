def diviseurdeliste(liste):
    lengh=len(liste)//3
    a=liste[:lengh]
    b=liste[lengh:lengh*2]
    c=liste[lengh*2:]
    return a,b,c
def inverse(liste):
    newliste=[]
    i=len(liste)-1
    while(i>=0):
        newliste.append(liste[i])
        i-=1
    return newliste
liste=[11, 45, 8, 23, 14, 12, 78, 45, 89]
l1,l2,l3=diviseurdeliste(liste)
print(inverse(l1),end="")
print(inverse(l2),end="")
print(inverse(l3))