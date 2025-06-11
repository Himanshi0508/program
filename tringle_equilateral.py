a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if(a==b and b==c and c==a):
    print("equilateral tringle")
elif(a==b!=c or a!=b==c or a==c!=b):
    print("isosceles tringle")   
elif(a!=b!=c!=a):
    print("scalene tringle")   
else:
    print("not valid tringle")    