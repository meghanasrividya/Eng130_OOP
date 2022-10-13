# create a function *
# This function takes two arguments from the user and provides the multiplication
def multiplication(arg1,arg2):
    mul=arg1 * arg2;
    return mul
# create a function %
# This function takes two arguments from the user and provides the remainder when arg1 is divided by arg2
def remainder(arg1,arg2):
    rem=arg1 % arg2;
    return rem
# create a function *
# This function takes two arguments from the user and provides the quotient
def division(arg1,arg2):
    div=arg1 / arg2;
    return div
# Prompt the user to input first number
arg1 = int(input("Please enter the first number : "))
# Prompt the user to input first number
arg2 = int(input ("Please enter the second number : "))
# Prompt the user to select the operation
opt = input("Please select one of the operation from *,%,/: " )

if opt=='*':
    print(multiplication(arg1,arg2))
elif opt=='%':
    print(remainder(arg1,arg2))
elif opt=='/':
   print (division(arg1,arg2))
else:
    print("Enter the proper option:")

