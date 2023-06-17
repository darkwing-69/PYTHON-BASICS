#A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
a=int(input("Enter your qty:"))
cst=100*a
if a>1000:
    b=10/100*cst
    c=cst-b
    print("The actual cost:",cst)
    print("The Bonus amnt you got:",b)
    print("Congrts you got bonus your final cost will be:",c)
else:
    print("no bonus your actual cost will be:",cst)

OUTPUT:
Enter your qty:980
no bonus your actual cost will be: 98000

Enter your qty:1100
The actual cost: 110000
The Bonus amnt you got: 11000.0
Congrts you got bonus your final cost will be: 99000.0



