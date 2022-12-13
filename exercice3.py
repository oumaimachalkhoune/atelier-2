Liste=[11, 45, 8, 11, 23, 45, 23, 45, 89]
a=[]
my_dict = {} 
for i in range (len(Liste)-1):
    k=0
    for j in range (len(Liste)-1):
        if Liste[i]==Liste[j]: 
            k+=1  
    a.insert(i,k)
for i in range (len(Liste)-1):
    my_dict.setdefault(Liste[i],a[i])
my_dict.setdefault(Liste[-1],a[-1])
print(my_dict)