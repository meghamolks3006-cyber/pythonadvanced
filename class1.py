# class person:
#
#     def __init__(self,n,a):#__init__used to create and initialize object properties
#         self.name=n
#         self.age=a
#     def show(self):      #self represent current object
#         print(self.name,self.age)
# p1=person("megha",22)     #create object of class person
# p1.show()
# p2=person("arjun",24)
# p2.show()

#
#
#
# class person:
#
#     def __init__(self):  #__init__used to create and initialize #object attributes/properties
#         self.name=input("enter name")
#         self.age=int(input("enter age"))
#     def show(self): #self represenys current object 2 usages
#         print(self.name,self.age)
#
#         #dynamic input
# p1=person()#create object of class person
#             # it will call __init()automatically
# p1.show()
# p2=person() #create object of class person
#               #it will call __init__() automatically
# p2.show()


#define a class named employee with attribute empid,name,age,place,salary,designation and methods getsalary()
# and showpersonaldetails()create an employee object and call the methods
# class employee:
#
#     def __init__(self):
#          print("enter employee details:")
#         self.empid = int(input("Enter employee ID: "))
#         self.name = input("Enter name: ")
#         self.age = int(input("Enter age: "))
#         self.place = input("Enter place: ")
#         self.salary = float(input("Enter salary: "))
#         self.designation = input("Enter designation: ")
#
#     def getsalary(self):
#         print("Salary:", self.salary)
#
#     def showpersonaldetails(self):
#         print("Employee ID:", self.empid)
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Place:", self.place)
#         print("Designation:", self.designation)
#
#
# # dynamic input
# e1 = employee()       # create object of class employee
#                        # it will call __init__() automatically
#
# e1.getsalary()
# e1.showpersonaldetails()

#define a class named student with attributes rollno,name,mark1,mark2,mark3,and method display() to display roll no
#and total mark of a student create 2 student objects and call the methods
# class student:
#
#     def __init__(self):
#         print("Student details:")
#         self.rollno = int(input("Enter roll number: "))
#         self.name = input("Enter name: ")
#         self.mark1 = int(input("Enter mark 1: "))
#         self.mark2 = int(input("Enter mark 2: "))
#         self.mark3 = int(input("Enter mark 3: "))
#
#     def display(self):
#         print("Roll number:", self.rollno)
#         print("Name:", self.name)
#         print("Total marks:", self.mark1 + self.mark2 + self.mark3)
#
#
# # Dynamic input
#
# s1 = student()
# s1.display()
#
# s2 = student()
# s2.display()


#define a class named book with attributes title,author,price,pages,languages and methods gettitle(),getauthor(),getprice()
#settitle(),setauthor(),setprice()
#create book object and call the methods
class book:

    def __init__(self):
        self.title = input("Enter title: ")
        self.author = input("Enter author: ")
        self.price = float(input("Enter price: "))
        self.pages = int(input("Enter number of pages: "))
        self.languages = input("Enter language: ")

    def gettitle(self):
        print( self.title)

    def getauthor(self):
        print( self.author)

    def getprice(self):
        print( self.price)

    def settitle(self):
        self.title = input("Enter new title: ")
        self.gettitle()
    def setauthor(self):
        self.author = input("Enter new author: ")
        self.getauthor()
    def setprice(self):
        self.price = float(input("Enter new price: "))
        self.getprice()

b=book()
b.gettitle()
b.settitle()


# print("Updated details:")
# b1.gettitle()
# b1.getauthor()
# b1.getprice()