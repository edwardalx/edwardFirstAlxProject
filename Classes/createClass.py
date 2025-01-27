class  Animals():                                                            #Decalre the class
    def __init__(self, name, age):                                         # Create a constructor
        self.name = name                                                   # initialise artributes
        self.age  = age
    
    def ageDecade(self, x):                                                 
        return f"has a max of {x} decades of life expectancy"
    
myAnimal = Animals("Dogs",30)                                              #objects creation
    
print(myAnimal.name,myAnimal.ageDecade(myAnimal.age)  )                     #Call the class


class Country(Animals):

    def orgCountry(self, x):                                                  
        return f"They are mainly found in  {x}"
    

class Food(Animals):
    def favFood(self, x):
        return f"They're favourite food is {x}"
    
myAnimalOrigin = Country("country", 20)
myAnimalFood = Food("food",  20)

print(myAnimal.name,myAnimal.ageDecade(myAnimal.age), myAnimalOrigin.orgCountry("Kenya"), myAnimalFood.favFood("Pawpaw"))


# class Country(Animals):

#     def ageDecade(self, x):                                                  
#         return f"They are mainly found in  {x}"
    

# class Food(Animals):
#     def ageDecade(self, x):
#         return f"They're favourite food is {x}"
# tryLoop = [
#     Country("country", 20),  Food("food",  20)
# ]
# for item in tryLoop:                                                                                 # Polymorhism
#     print( item.ageDecade("Edwrad"))
