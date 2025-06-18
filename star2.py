n=int(input("enter the number"))
for i in range (0,n-1):
    str=" "
    for j in range (n-(i+1)):
        str+=" *"
    print(str)    