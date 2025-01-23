class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __del__(self):
        print('Object is being deconstructed')

p = Person('Test', 25)

class Vector:
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    def __add__(self, other): 
        return Vector(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f'X: {self.y}, Y: {self.y}'
    def __call__(self):
        print('Hello I was called')

v1 = Vector(10,20)
v2 = Vector(30,40)
v3 = Vector(50,60)

#v2()
v3()
## advace python video by neuralnine