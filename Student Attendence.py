a=int(input("Enter no of cls held:"))
b=int(input("Enter no of cls  attended:"))
p=b/a*100
print("your percentage will  be:",p)
if p<75:
    print("Your not allowed to write exam your attendence is less than  75%")
else:
    print("you are allowed to  write exam")

OUTPUT:
Enter no of cls held:100
Enter no of cls  attended:32
your percentage will  be: 32.0
Your not allowed to write exam your attendence is less than  75%

Enter no of cls held:110
Enter no of cls  attended:90
your percentage will  be: 81.81818181818183
you are allowed to  write exam


