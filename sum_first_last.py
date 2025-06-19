number=int(input("enter the number"))
original_num=number
if number<0:
    last_digit= -(-number %10)
else:
    last_digit=number %10     
first_digit=number
for i in range(1,number):
    if(first_digit >=10 or first_digit<= -10):
        first_digit = first_digit//10        
sum=first_digit+last_digit
print(first_digit) 
print(last_digit)                 
print(sum)