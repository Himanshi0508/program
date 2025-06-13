total=0
n=int(input("enter the number"))
for i in range (0,n+1):
    if(i%2==0):
     total+=i
     print("total even number",total)