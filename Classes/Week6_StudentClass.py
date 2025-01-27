class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"student name  and age are: "
    def student_info():
        print(f"student name  and age are: ")

# myStudent = Student("Bismark", 36)

# # print(myStudent)

class Product:
    def __init__(self, name, price, quantity):
        self.student = Student("Edward", 31)
        self.name = name
        self.price = price
        self.quantity = quantity
    def total(self, y, z):
        return  y * z
    # def studentInfor(self):
    #     return self.student.student_info
myProduct = Product("Cement", 100, 50)
print(myProduct.student)

print(
    f"I am {myProduct.student.name} of {myProduct.student.age}", 
    f"The cost of {myProduct.quantity} bags of  {myProduct.name} is {myProduct.total(myProduct.quantity, myProduct.price)}" 
      )