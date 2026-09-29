#Ask the user to enter a number.if the number is less than or equal to 0,
# raise a ValueError with the message "Number must be Positive"
try:
    num=int(input("enter number"))
    if(num<=0):
        raise ValueError("number must be positive")
    else:
        print(num)
except ValueError as e:
    print(e)


#Ask the user to enter a password.if its length is less than 8 characters ,raise
#a customexception InvalidPasswordError with the message ("Password should be 8
# characters")

class InvalidPasswordError(Exception):
    pass

try:
    password=input("enter password")
    if(len(password)<8):
        raise InvalidPasswordError("Password should be 8 characters")
    else:
        print("Valid Password")
except InvalidPasswordError as e:
    print(e)



#Ask the user to enter an amount and if the amount<balance ,raise customException
#InsuffientBalanceError with the message("Not Enough Balance.Transaction Failed")
class InsuffientBalanceError(Exception):
    pass

try:
    balance=5000
    amount=int(input("enter amount"))

    if(amount>balance):
        raise InsuffientBalanceError("Not Enough Balance.Transaction Failed")
    else:
        print("Transaction Successful")
except InsuffientBalanceError as e:
    print(e)