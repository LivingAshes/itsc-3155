#program 3

dicta = input("Input first dictionary: ")
dictb = input("Input second dictionary: ")
dict1 = eval('dict(% s)' % dicta)
dict2 = eval('dict(% s)' % dictb)
outdict = dict1
for key, value in dict2.items() :
    if key in outdict :
        outdict[key] = value + outdict.get(key)
    else :
        outdict[key] = value
print(outdict)
