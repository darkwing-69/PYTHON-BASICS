# To check wether the given time is Morning ,afternoon,evening,Night
Time=float(input("Enter Your time:"))
if Time<12.00:
    print("Its Morning")
elif Time>12.00 and Time<15.59:
    print("Its Afternoon")
elif Time>16.00 and Time<18.59:
    print("Its Evening")
else:
    print("Its Night")

output:

Enter Your time:8.00
Its Morning

Enter Your time:13.29
Its Afternoon

Enter Your time:20.09
Its Night
