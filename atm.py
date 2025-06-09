available_amount=int(input("enter the amount"))
withdraw_amount=int(input("enter the cash"))
bankcharge=0.50
withdraw=withdraw_amount+bankcharge
if(available_amount>=withdraw):
    if(withdraw_amount%5==0):
       availableAmount= available_amount-withdraw
       print("amount withdraw  successfully,your available amount is",availableAmount)
    else:
        print("withdraw amount is not divisible by 5 ")
else:
    print("ensufficint amount")