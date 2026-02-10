#  Implement a class Employee with attributes name and salary and a method to apply a 10% raise.

class Employee:
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    def increase_salary(self):
        return self.salary+self.salary*0.1
    
    def showEmployee(self):
        print(f"Salary of employee {self.name} after 10% salary increment is {self.increase_salary()}")
        
e1=Employee("Ram",10000)
e1.increase_salary()
e1.showEmployee()