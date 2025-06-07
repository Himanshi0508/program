selling_price=int(input("enter the selling price"))
cost_price=int(input("enter the cost price"))
a=selling_price-cost_price
if(a>0):
    print("profit")
elif(a<0):
    print("loss")    
else:
   print("zero")    