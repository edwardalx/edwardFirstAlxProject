class ValueTooHighError(Exception):
    def __init__(self, x):
        self.x = x
    
    def __str__(self):
        return f"Your number {self.x} is greater than 100"
    
def myNumber():
        myInput = int(input("Enter a number: "))
        try:
            if myInput <= 100:
                print(f"The numner you entered is {myInput}")
            else:
                raise ValueTooHighError(myInput)
        except ValueTooHighError as e:
            print(e)
        except ValueTooHighError:
            print("Please enter a numerical value")


myNumber()

def myNumber2():
    while True:
        try:
            myInput = int(input("Enter a number: "))
            if  myInput <= 100:
                print(f"The numner you entered is {myInput}") 
                break   
            else:
                raise ValueTooHighError(myInput)     #pass your input in the created exception
        except ValueTooHighError as e:
            print(e)
        except ValueTooHighError:
            print("Please enter a numerical value")

myNumber2()

