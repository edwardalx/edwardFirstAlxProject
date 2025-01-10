def loopDict(i,j):
    for x in i:
        if i[x] == j:
            return x
    return dict()

a = ["v1", "v2", "v3", "v4", "v5", "v6"]
b = [2,4,11,1,5,6,11]
myDict = dict(zip(a,b))
print(myDict)
print(loopDict(myDict,1))
print(loopDict(b,11))
