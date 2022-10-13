def fizzbuzz(ran) :
    for i in range (1,ran) : print ("Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i))

ran = int(input("Please enter the range :"))

fizzbuzz(ran)