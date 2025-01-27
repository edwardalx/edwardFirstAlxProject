class Duck:
    def quack(self):
        return "Duck quacks"

class Person:
    def quack(self):
        return "Person imitates duck"

# Polymorphic behavior using duck typing
def make_sound(obj):
    return obj.quack()

def my_poly(a, b):
    return f"{a.quack()} and {b.quack()}"

# duck_obj = Duck()
# person_obj = Person()

# print(make_sound(duck_obj))    # Output: "Duck quacks
# print(make_sound(person_obj))  # Output: "Person imitates duck"
# print(my_poly(duck_obj,person_obj))

myDucks = [Duck(),Person()]
for myDuck in myDucks:
    print (my_poly(myDuck, myDuck))