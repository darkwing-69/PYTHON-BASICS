# To Enter Login Credtionals with a strong passowrd
a=(input("Enter your Mail id:"))
b=(input("Enter your password:"))
c=len(b)
if c<5:
   print("Password Declined")
   print("Your Password Needs to Be Minimum 5 Characters")
elif c>=5:
      if b.isalpha():
         print("Password Declined")
         print("Passowrd needs to be mixed of numerical characters")
      else:
          if b.isnumeric():
             print("Password Declined")
             print("Passowrd needs to be mixed of alphabatical characters")   
          else:
              if b.istitle():
                 print("Strong Password")
                 print("Password Approved")
              else:
                  print("Password Declined")
                  print("The first case should be capital")


OUTPUT:
Enter your Mail id:runoutarun15@gmail.com
Enter your password:Thanos
Password Declined
Passowrd needs to be mixed of numerical characters

Enter your Mail id:runoutarun15@gmail.com
Enter your password:Thanos1234
Strong Password
Password Approved




             
