# list
myList = [2,3,5,11,12,17]
myList.append(77)
myList.insert(0, 3)
print(myList)
myNewList = []
#slicing  first index inclusive last index exclusive
mySlice = myList[1:4]
# slicing with steps
mySLice_ = myList[::2]
#slicing Reverse 
mySLiceRev= myList[::-1]
print(mySLiceRev)


myTuple= (2,3,4,5,6,7,8)  #Tuple
print(type(myTuple))


#Set
mySetA = {2,3,5,11,12,17,77, 17, 12, 11, 5, 3, 2, 3}
mySetB = {77, 17, 12, 11, 5, 3, 2, 3}
c = mySetA.intersection(mySetB)
d = mySetA.union(mySetB)
print(mySetA)
print(d)

#Data Conversion
newList = list(mySetB)
newListB = tuple(mySetB)
print(newListB)

#Dictionary
myDict = {"k1":"v1","k2":"v2","k3":"v3","k4":"v4"}
#print(myDict["k1"])
#print(myDict)
myDict["k3"],myDict["k1"]= "Edward",5
print(myDict)