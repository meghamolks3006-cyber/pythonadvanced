#write a menu driven code for bank operation
#using class and list
#1.create a new account
# 2.withdraw
# 3.deposit
# 4.showbalance
# 5.exit
# class Account:
#
#     def __init__(self):
#         print("Account details")
#         self.acctnumber = int(input("Enter account number: "))
#         self.acctname = input("Enter account name: ")
#         self.balance = float(input("Enter balance: "))
#
#     # Operations
#
#     def showbalance(self):
#         print("Current balance:", self.balance)
#
#     def withdraw(self):
#         amount = float(input("Enter amount to withdraw: "))
#
#         if amount > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance = self.balance - amount
#             self.showbalance()
#
#     def deposit(self):
#         amount = float(input("Enter amount to deposit: "))
#         self.balance = self.balance + amount
#         self.showbalance()
#  l=[]
# while(1):
#     print("bank operations")
#     print(1."create a new account")
#     print(2."withdraw")
#     print(3."deposit")
#     print(4."showbalance")
#     print(5."exit")
#     ch=int(input("Enter your choice: "))
#
#     if ch==1:
#         a=Account()
#         l.append(a) #saves each account objects into a list
#         print(l)
#     elif ch==2:
#         number=int(input("Enter account number: "))
#
#         for i in l:
#             if(i.acctnumber==number):
#                 i.withdraw()
#     else:
#         print("account does not exit")
#     elif ch==3:
#     number = int(input("Enter account number: "))
#
#     for i in l:
#         if (i.acctnumber == number):
#             i.deposite ()
#             break
# else:
#           print("account does not exit")
#     elif ch==4:
# number=int(input("Enter account number: "))
#
#         for i in l:
#             if(i.acctnumber==number):
#                 i.showbalance()
#                 break
#     else:
#         print("account does not exit")
#     else:
#         exit()


#write a menu driven code for bank operation
#using class and list
#1.create a new account
#2.withdraw
#3.deposit
#4.showbalance
#5.exit


class Account:

    def __init__(self):
        print("Account details")
        self.acctnumber = int(input("Enter account number: "))
        self.acctname = input("Enter account name: ")
        self.balance = float(input("Enter balance: "))

    # Operations

    def showbalance(self):
        print("Current balance:", self.balance)

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))

        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance - amount
            self.showbalance()

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance = self.balance + amount
        self.showbalance()


l = []

while(1):
    print("bank operations")
    print("1. create a new account")
    print("2. withdraw")
    print("3. deposit")
    print("4. showbalance")
    print("5. exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        a = Account()
        l.append(a) # saves each account object into a list
        print(l)

    elif ch == 2:
        number = int(input("Enter account number: "))

        for i in l:
            if(i.acctnumber == number):
                i.withdraw()
                break
        else:
            print("account does not exist")

    elif ch == 3:
        number = int(input("Enter account number: "))

        for i in l:
            if(i.acctnumber == number):
                i.deposit()
                break
        else:
            print("account does not exist")

    elif ch == 4:
        number = int(input("Enter account number: "))

        for i in l:
            if(i.acctnumber == number):
                i.showbalance()
                break
        else:
            print("account does not exist")

    elif ch == 5:
        print("Thank you")
        break

    else:
        print("Invalid choice")





#Write a menu-driven Python program using a class Student
    #to perform the following operations:
#
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.

# Write a menu-driven Python program using a class Student
# to perform the following operations:
#
# 1. Add Student(roll no, name, marks)
# 2. Update Marks
# 3. Display All Student Details
# 4. Search Student by Roll Number
# 5. Delete Student
# 6. Exit
#
# Store student records in a list and perform all operations
# using the student's roll number.


class Student:

    def __init__(self):
        print("Student details")
        self.rollno = int(input("Enter roll number: "))
        self.name = input("Enter student name: ")
        self.marks = float(input("Enter marks: "))

    # Operations

    def update(self):
        self.marks = float(input("Enter new marks: "))
        print("Marks updated successfully")

    def display(self):
        print("Roll Number:", self.rollno)
        print("Name:", self.name)
        print("Marks:", self.marks)

    def search(self):
        print("Roll Number:", self.rollno)
        print("Name:", self.name)
        print("Marks:", self.marks)


l = []

while(1):
    print("\nStudent operations")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Display All Student Details")
    print("4. Search Student by Roll Number")
    print("5. Delete Student")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        s = Student()
        l.append(s)  # saves each student object into a list
        print("Student added successfully")

    elif ch == 2:
        number = int(input("Enter roll number: "))

        for i in l:
            if(i.rollno == number):
                i.update()
                break
        else:
            print("Student does not exist")

    elif ch == 3:
        for i in l:
            i.display()

    elif ch == 4:
        number = int(input("Enter roll number: "))

        for i in l:
            if(i.rollno == number):
                i.search()
                break
        else:
            print("Student does not exist")

    elif ch == 5:
        number = int(input("Enter roll number: "))

        for i in l:
            if(i.rollno == number):
                l.remove(i)
                print("Student deleted successfully")
                break
        else:
            print("Student does not exist")

    elif ch == 6:
        print("Thank you")
        break

    else:
        print("Invalid choice")

