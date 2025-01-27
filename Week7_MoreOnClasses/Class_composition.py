class Car:
  def __init__(self, engine):
    self.engine = engine  # Engine object as an attribute

  def start1(self):
    print("I am eddy the ego")
    # self.engine.start()

class Engine:
  def __init__(self,age):
    self.age = age
  def start(self):
    print("Engine starting...")

# car = Car(Engine())
# car.start1()  # Output: Engine starting...

car = Car("x")
engine1 = Engine(car)
engine1.st