'''
Constructors (__init__)
Destructors (__del__)
Magic Methods (e.g., __str__, __repr__)
'''

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"x-cordinate: {self.x}, y-cordinate: {self.y}"
    
    def mydiv(self):
        return
    

# pointA = Point(1,10)
# print(f"Point coordinates: ({pointA.x}, {pointA.y})")  # Output: Point coordinates: (3, 5)
# print(pointA.y)
# print(pointA)
class Transformation(Point):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.a = a
        self.b = b
    def __str__(self):
        return f"The image of point A ({traslate.x}, {traslate.y}) is {traslate.translation(traslate.x, traslate.a),traslate.translation(traslate.y, traslate.b) }"
    def translation(self, a, b):
        image = a + b
        return image

  
    
traslate = Transformation(5,4,2,2)
print(traslate)

class Enlargement(Transformation):
    def __init__(self, x, y, a, b, k):
        super().__init__(x, y, a, b)
        self.k = k
    def __str__(self):
        return f"The image of point A  ({enlarge.k},{enlarge.x}), under an enlargement by scale factor {enlarge.k} is {enlarge.enlargePoint(enlarge.x, enlarge.k),enlarge.enlargePoint(enlarge.y,enlarge.k)}"
    
    def enlargePoint(self, x, k):
        image = x * k
        return image
    
enlarge = Enlargement(5,4,2,2,10)
print(enlarge)
