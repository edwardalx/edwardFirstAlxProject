class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def get_age(self):
        return self._age
    
    @get_age.setter
    def set_age(self, new_value):
        self._age = new_value



student1 = Student("Bismark", 20)
student1.set_age = 30

print(student1.set_age)


