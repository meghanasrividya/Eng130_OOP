def odd_even_counter(range1):
    for i in range(1,range1) :  print("even"*( i%2==0) or str(i))


range1 = int(input("Enter the range of the number:"))
odd_even_counter(range1)