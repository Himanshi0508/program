n=int(input("enter the number"))
total=0
for i in range(1,n+1):
    if(n%i==0):
         total= total+i
print(total)