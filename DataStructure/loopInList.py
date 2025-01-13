a = ["v1", "v2", "v3", "v4", "v5", "v6"]

def loopList(y):
        for z in range(1,6):
            if a[z] == y:
             return z
      
print(loopList("v2"))


#Alternatively

a = ["v1", "v2", "v3", "v4", "v5", "v6"]
print(a.index("v2"))