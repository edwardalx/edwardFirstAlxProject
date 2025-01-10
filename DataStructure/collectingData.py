myDataName = []
myDataAge  = []

# x = 1
# while x < 10:
#     myData.append(x)
#     x=x+1
# print(myData)

def  collectData():
    while True:
        name = input("Whats is your name(enter Exit to quit): ")
        if name != "exit":
            myDataName.append(name)
            try:
               age = int(input("How old are you: "))
               myDataAge.append(age)
            except(ValueError):
                print("Please enter a number")
        print(f"The name you've entered is {myDataName[len(myDataName)-1]} and age is {myDataAge[len(myDataAge)-1]}")
        myData = dict(zip(myDataName,myDataAge))
        print(myData)
        if name == "exit":
            break
       
collectData()



