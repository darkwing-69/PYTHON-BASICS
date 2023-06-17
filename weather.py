# To check the weather accrding to the temperature
wthr=float(input("Enter The temperature  in celsius:"))
if wthr>=35 and wthr<=49:
    print("According to  this temp weather will be too hot")
elif wthr>=30 and wthr<=34:
    print("Accordinng to his temp  weather will be humid")
elif wthr>=20 and wthr<=28:
    print("According to this temp weather will be two cold")
else:
    print("No  records Found")
    
OUTPUT:

Enter The temperature  in celsius:42
According to  this temp weather will be too hot

Enter The temperature  in celsius:32
Accordinng to his temp  weather will be humid

Enter The temperature  in celsius:22
According to this temp weather will be two cold

