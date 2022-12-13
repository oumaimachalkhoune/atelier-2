
def verificationdelements(list,dict):
    res = []
    for x in dict.keys():
        if dict[x] in list:
            res.append(dict[x])
    return res

list = [47, 64, 69, 37, 76, 83, 95, 97]
dict = {'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97}

print(verificationdelements(list, dict))