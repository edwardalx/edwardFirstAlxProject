class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def student_info():
        print(f"student name  and age are: ")

myStudent = Student("Bismark", 36)

print(myStudent.name)

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total(self, y, z):
        return  y * z
myProduct = Product("Cement", 100, 50)

print(f"The cost of {myProduct.quantity} bags of  {myProduct.name} is {myProduct.total(myProduct.quantity, myProduct.price)}" )