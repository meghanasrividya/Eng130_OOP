def twin(a,b):
    if (sorted(a)==sorted(b)):
         return True
    else:
        return False
a=input("Enter the word 1:")
b=input("Enter the word 2:")

if( twin(a,b)):
    print("The two words you entered are twins")
else:
    print("The two words you entered are not twins")