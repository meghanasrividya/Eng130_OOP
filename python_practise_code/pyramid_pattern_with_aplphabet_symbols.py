n=int(input("Enter the number of rows:"))

for i in range(n):
     print (" "*(n-1-i),end=' ')
     for j in range(i+1):
          print(chr(64+n-j),end=' ')

     print()