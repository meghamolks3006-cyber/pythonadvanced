#1.Create a class named Circle with an attribute radius. Use a constructor to initialize the radius by accepting input from the user. Define the following methods:

# getarea() – to calculate and display the area of the circle.
# getperimeter() – to calculate and display the perimeter (circumference) of the circle.
#
# Create an object of the Circle class and call both methods to display the results.

# #
# class circle:
#
#     def __init__(self):
#         self.radius = input("Enter radius: ")
#
#     def getarea(self):
#         print("Area =", 3.14 * int(self.radius) * int(self.radius))
#
#     def getperimeter(self):
#         print("Perimeter =", 2 * 3.14 * int(self.radius))
#
#
# # Create Circle object
#
# c = circle()
# c.getarea()
# c.getperimeter()
#
# c1 = circle()
# c1.getarea()
# c1.getperimeter()
#
# 2.Create a class named Account with attributes acctnumber, acctname, and balance. Initialize these values using a constructor by taking input from the user. Define the following methods:
#
# withdraw() – to withdraw an amount from the account and update the balance.
# deposit() – to deposit an amount into the account and update the balance.
# showbalance() – to display the current balance of the account.
#
# # Create an object of the class and call the methods to perform withdrawal and deposit operations and display the updated balance.
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


a1 = Account()

a1.withdraw()
a1.deposit()
a1.showbalance()

a2 = Account()














# l=[10,20,30]
# for i in l:
#     print(i)
#
# l=["red","green","blue"]
# for i in l:
#     print(i)

# l=[a1,a2]
# for i in l:
#     #for all objects
#     print(i.acctnumber, i.acctname, i.balance)  #to print object(i.propertyname)
#
# #to call particular  object (showbalance)
# for i in l:
# if(i.acctnumber == 123):
#     i.showbalance()