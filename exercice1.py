

liste1=[3, 6, 9, 12, 15, 18, 21]
liste2=[4, 8, 12, 16, 20, 24, 28]
liste3=[]
for i in range(len(liste1)):
    if i%2!=0:
        print("i=",i)
        liste3.append(liste1[i])
        print(liste3)
for i in range(len(liste1)):
    if i%2==0:
        print("i=",i)
        liste3.append(liste2[i])
        print(liste3[i])
print('liste1=',liste1)
print('liste2=',liste2)
print('liste3=',liste3)
