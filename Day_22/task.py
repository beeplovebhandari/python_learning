class Circle:
    def __init__(self, radius):
        self.radius = radius

    def add_radius (self, obj2):
        return self.radius + obj2.radius
    
    def __add__ (self, other):
        return self.radius + other.radius

c1 = Circle(10)
c2 = Circle(12)
result = c1.radius + c2.radius
print(result) # 22

result = c1.add_radius(c2)
print(result) # 22

result = c1 + c2
print(result) # 22
