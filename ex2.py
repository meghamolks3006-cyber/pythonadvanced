# try:
#     num1 = int(input("enter a number"))
#     num2 = int(input("enter another number"))
#     r=num1+num2
#     print("result",r)
# except ZeroDivisionError:
#     print("Zero Division Error")
# except ValueError:
#     print("Value Error")
# except: #general code if any exception other than above two
#     print("Error")



# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input
import math

while True:
    try:
        n = int(input("Enter a number: "))
        r = math.factorial(n)
        print("Factorial", r)
        break

    except:
        print("Invalid input")

#Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
#and division based on user choice. Handle invalid inputs and division by zero using exception handling.
while True:
    try:

        print("1. addition")
        print("2. subtraction")
        print("3. multiplication")
        print("4. division")
        print("5. exit")

        ch = int(input("Enter your choice: "))

        if ch in [1, 2, 3, 4]:
            n = int(input("Enter number: "))
            m = int(input("Enter a number: "))

            s = n + m
            d = n - m
            p = n * m
            q = n / m

    except ZeroDivisionError:
        print("Zero Division Error")

    except ValueError:
        print("Value Error")

    except:
        print("Error")

    else:

        if ch == 1:
            print("Result", s)

        elif ch == 2:
            print("Result", d)

        elif ch == 3:
            print("Result", p)

        elif ch == 4:
            print("Result", q)

        elif ch == 5:
            exit()

        else:
            print("Invalid choice")

# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist
try:
    f = open("sample.txt", "r")
    print(f.read())
    f.close()

except FileNotFoundError:
    print("File does not exist")


#Given a Dictionary
#
# d={"name':"arun","age":23,"place":"ekm"}
# Write a program to ask the user to enter a key and display its value.
# Handle KeyError if key does not exist
d = {"name": "arun", "age": 23, "place": "ekm"}

try:
    key = input("Enter a key:")
    print("Value:", d[key])

except KeyError:
    print("Key does not exist")