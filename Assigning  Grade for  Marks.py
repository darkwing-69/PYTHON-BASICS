# assigning grades (A, B, C) based on marks obtained by a student.
Mark=int(input("Enter Your Marks:"))
percent=Mark/500*100
print("Your percentage will be:",percent)
if percent>90:
    print("Congrats your grade is A")
elif percent>75:
    print("Congrats your grade is B")
elif percent>65:
    print("Congrats your grade is C")
else:
    print("Sorry no grade assigned")

OUTPUT:
Enter Your Marks:386
Your percentage will be: 77.2
Congrats your grade is B

