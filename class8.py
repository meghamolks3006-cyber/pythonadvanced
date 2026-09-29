

# class person:
#     def __init__(self):
#        self.name = input("Enter your name:")
#        self.age = input("Enter your age:")
#
# class student(person):
#     def __init__(self):
#         super().__init__()
#         self.rollno = input("Enter your roll no:")
#         self.course = input("Enter your course:")
#         self.marks = input("Enter your marks:")
#
# s = student()

########################################################3
class person:
    def __init__(self):
       self.name = input("Enter your name:")
       self.age = input("Enter your age:")
    def show(self):
        print(self.name,self.age)

class student(person):
    def __init__(self):
        super().__init__()
        self.rollno = input("Enter your roll no:")
        self.course = input("Enter your course:")
        self.marks = input("Enter your marks:")
    def show(self):
        super().show()
        print(self.rollno,self.course,self.marks)
    def updatemarks(self):
        self.marks = input("Enter your new marks:")
s=student()
s.show()
s.updatemarks()

##############################################################################

# 1. Company -> Employee Hierarchy


class Company:
    def __init__(self):
        self.company_name=input("Enter Company Name:")
        self.location=input("Enter Location:")
    def display_company(self):
        print(self.company_name,self.location)

class Employee(Company):
    def __init__(self):
        super().__init__()
        self.empid=int(input("enter empid:"))
        self.name=input("Enter name:")
        self.designation=input("Enter Designation:")
        self.salary=int(input("Enter Salary:"))
    def display_details(self):
        super().display_company()
        print(self.empid,self.name,self.designation,self.salary)
    def update_salary(self):
        self.salary=1.1*self.salary
        print("Updated Salary:",self.salary)

e=Employee()
e.display_details()
e.update_salary()


# ==========================================
# 2. Category -> Product Hierarchy
# ==========================================

class Category:
    def __init__(self):
        self.category_name = input("Enter category name: ")

    def show_category(self):
        print("Category Name:", self.category_name)


class Product(Category):
    def __init__(self):
        super().__init__()
        self.product_name = input("Enter product name: ")
        self.price = float(input("Enter price: "))
        self.quantity = int(input("Enter quantity: "))

    def total_price(self):
        super().show_category()
        print("Product Name:", self.product_name)
        total = self.price * self.quantity
        print("Total Product Price:", total)


# --- Category/Product Execution ---
print("--- PRODUCT DETAILS ---")
prod = Product()
prod.total_price()
