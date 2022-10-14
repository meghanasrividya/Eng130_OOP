# Python Object Oriented Programming 
- Python is a multi-paradigm programming language. It supports different programming approaches.

- One of the popular approaches to solve a programming problem is by creating objects. This is known as Object-Oriented Programming (OOP).
- The concept of OOP in Python focuses on creating reusable code. This concept is also known as DRY (Don't Repeat Yourself).
## 4 Pillars of OOP
- Four pillars of python are Abstraction , Encapsulation, Inheritance,Polymorphism
#### Abstraction:
- Abstraction is one of the most important features of object-oriented programming. It is used to hide the background details or any unnecessary implementation.
#### Inheritance:
- Inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).
#### Polymorphism:
- Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
#### Encapsulation:
- Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. 
Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle). However we could use the same method to color any shape. This concept is called Polymorphism.
### methods/functions
#### Modules
##### Lib-Packages

#### use case -benefits-examples of builtin
- A built-in function is a function that is already available in a programming language.
- Python functions work very simply. You call the function and specify the required arguments, then it will return the results.
#### Program to round the number using built in methods
```python
import math
number = 23.66
# to compute any numbers to round the figure up
#numbers 1.50 above to round up to 2
#numbers 1.49 or less round down to 1

print(math.ceil(number))# ceil will round the figure up
print(math.floor(number))#floor will help you round the figure to bottom

```
#### Build the simple calculator
```python
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


```
- step 1: create animal.py as parent
  
- step 2: create reptile.py as a child to inherit-abstract etc
- step 3: snake.py & inherit from reptile
- step 4: python_oop.py 
 ```
```