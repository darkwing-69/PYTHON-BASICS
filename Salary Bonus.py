#To Give Bonus if they reached The Monthly Target
Tar=int(input("Enter your sale count:"))
sal=int(input("Enter your salary:"))
if Tar<30:
    print("Sorry no bonus better luck next time")
elif Tar>30:
    salr=sal+5000
    print("Congrats you got your bonus")
    print("your salary will be:",salr)

OUTPUT:
Enter your sale count:12
Enter your salary:13000
Sorry no bonus better luck next time

Enter your sale count:32
Enter your salary:20000
Congrats you got your bonus
your salary will be: 25000


