def odd_even_counter(number):
   list_1=[0,0]

   while (number != 0) :
       if(number%2==0):
          list_1[0]=list_1[0]+number
       else:
            list_1[1]=list_1[1] + number

       number-=1
   return list_1

number =int(input("enter the value of number :"))
print(odd_even_counter(number))