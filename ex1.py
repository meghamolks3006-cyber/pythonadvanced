#sum of 2 numbers
try:
    num1=int(input("enter first number"))
    num2=int(input("enter second number"))
    s=num1+num2
except:
    print("invalid number")

#optional
else:
    print("sum",s)
finally:
    print("done")