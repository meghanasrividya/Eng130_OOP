class Student:
    def __init__(self,name,rollno,marks): # this is called constructor
        print("Constructor Execution....")
        """
        1. self is a reference variable, which is always pointing to current object .
        2. Within the python class, to access current object , we can use self.
        3. The first argument to the constructor is always self.
        4. We are not required to provide value for self variable,PVM(Python Virtual Machine) itself will provide value.
        5. We can use self always within the class only.
        6. self is not a keyword. we can use anyname like delf/kelf etc
        """
        print(id(self))
        self.name =name
        self.rollno = rollno
        self.marks = marks

    def talk(self):
        print("Hello I am:",self.name)
        print("My Roll number: ", self.rollno)
        print("My Marks are", self.marks)


s1 = Student("Sunny", 102, 99) # We are creating an object.PVM will create object and allocate memory.PVM will execute __init__()


print(id(s1))
print(s1.name)
print(s1.rollno)
print(s1.marks)
s1.talk()

s2 = Student("Bunny",103,98)
print(id(s2))
print(s2.name)
print(s2.rollno)
print(s2.marks)
s2.talk()