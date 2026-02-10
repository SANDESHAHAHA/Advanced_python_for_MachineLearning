#13. Create a class Rectangle with methods to calculate area and perimeter

class Rectangle:
    
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def area(self):
        return self.length*self.breadth
    
    def perimeter(self):
        return 2*(self.length+self.breadth)

l,b=float(input("Enter length: ")),float(input("Enter breadth"))
r1=Rectangle(l,b)
print(f"Perimeter: {r1.perimeter()}")
print(f"Area: {r1.area()}")
        