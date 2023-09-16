print("Welcome to Josets Pizza")

opinion= input("Would You Like to Buy a Pizza (Y/N)?")
if opinion == "Y" or opinion == "y":
    print(" 1:-small_pizza = 100 Ugshs \n 2:-medium_pizza = 200 Ugshs \n 3:-large_pizza = 300 Ugshs \n 0:- Am not Buying ")
    choose = int(input("Input The number of Your choice__"))
    if choose == 1:
        bill = 100
    elif choose == 2:
        bill = 200
    elif choose ==3:
        bill = 300
   
    extra= input("Would You Like Pepperoni on your pizza(Y/N)?")
    if extra == "Y" or extra == "y":
        if bill == 100:
            bill = bill + 30
        elif bill >100 :
            bill = bill + 50
    else:
        bill = bill
    
    cheese = input("Would You Like Cheese on your pizza(Y/N)?")
    if cheese == "Y" or cheese == "y":
        bill = bill + 20
else:
    bill = bill
    print("You can Request for a Bronchure for any other of our products.")

print(f"Your Bill is {bill} Ugsh.")

