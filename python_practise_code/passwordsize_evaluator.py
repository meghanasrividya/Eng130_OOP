def passwordsize_evaluator(password):
    if (len(password) <5):
           return "Your password is too short."
    elif(len(password) > 20):
        return "Your password is too long and may be forgotten"
    else:
        return "Your password is an acceptable length."


password=input("Enter the password:")

print(passwordsize_evaluator(password))