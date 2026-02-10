# 8. Implement a class Circle with a method to calculate the area and circumference. 

from math import pi

class Circle:
    
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return pi*(self.radius)**2
    
    def circumference(self):
        return 2*pi*self.radius

c1=Circle(5)
print(f"Circumference: {c1.circumference()}")
print(f"Area: {c1.area()}")