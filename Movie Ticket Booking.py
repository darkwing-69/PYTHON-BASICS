#TO Book A Ticket For Movie
a=input("Enter Your Movie Name:")
f=print('''Movie type:
            1)scifi
            2)Horror
            3)Drama
            4)Action
            5)Romance''')
b=input("Enter the Movie type:")
c=int(input("Enter Your age:"))
d=int(input("How many Members:"))

S="1"
H="2"
D="3"
A="4"
R="5"
if b==S:
      if c>10:
          print("per ticket costs 200")
          print("Your total cost will be",d*200)
          print("Enjoy Your Movie:)")
      else:
         print("sorry you are not allowed")
elif b==H:
    if c>=15:
        print("Per ticket costs 150")
        print("Your total cost will be",d*150)
        print("Enjoy Your Movie:)")
    else:
        print("Sorry you are not allowed")
elif b==D:
    if c>=12:
        print("Per ticket costs 100")
        print("Your total cost will be",d*100)
        print("Enjoy Your Movie:)")
    else:
        print("sorry you are not allowed")
elif b==A:
    if c>15:
        print("per ticket costs 250")
        print("Total cost will be",d*250)
        print("Enjoy your Movie:)")
    else:
        print("Sorry your Are not allowed inside")
else:
    if b==R:
        print("Sorry show not available Right Now")


    
OUTPUT :
Enter Your Movie Name:FAST AND FURIOUS
Movie type:
            1)scifi
            2)Horror
            3)Drama
            4)Action
            5)Romance
Enter the Movie type:4
Enter Your age:18
How many Members:7
per ticket costs 250
Total cost will be 1750
Enjoy your Movie:)

         
