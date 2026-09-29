#create an abstract class shape with abstarct method get_area() and get_perimeter()
#create 2 subclasses rectangle,square

from abc import ABC, abstractmethod

class shape(ABC):

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class rectangle(shape):

    def __init__(self):
        self.length = int(input("Enter length: "))
        self.breadth = int(input("Enter breadth: "))

    def get_area(self):
        print("Area:", self.length * self.breadth)

    def get_perimeter(self):
        print("Perimeter:", 2 * (self.length + self.breadth))


r = rectangle()
r.get_area()
r.get_perimeter()



#create an abstract class Employee with an abstract method calculate_salary()
# create two subclasses
# -FullTimeEmployee
# -PartTimeEmployee
# Each class should calculate salary differently.


from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):

    def __init__(self):
        self.salary = int(input("Enter monthly salary: "))

    def calculate_salary(self):
        print("Full Time Salary:", self.salary)


class PartTimeEmployee(Employee):

    def __init__(self):
        self.hours = int(input("Enter working hours: "))
        self.rate = int(input("Enter rate per hour: "))

    def calculate_salary(self):
        print("Part Time Salary:", self.hours * self.rate)


f = FullTimeEmployee()
f.calculate_salary()

p = PartTimeEmployee()
p.calculate_salary()