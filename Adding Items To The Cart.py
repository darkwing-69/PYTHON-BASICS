a=0
b='yes'
while b=='yes' and a<3:
           c=(input("Enter your product name:"))
           a+=1
d=input("do you wanna continue yes/no:")
if d=='yes':
   while b=='yes':
           c=(input("Enter your product name:"))
           d=input("do you wanna continue yes/no:")
           if d=='no':
                print(" Thanks For Shopping")
                break

elif d=='no':
     print(" Thanks For Shopping")

OUTPUT:
Enter your product name:RICE
Enter your product name:TOMATO
Enter your product name:POTATO
do you wanna continue yes/no:yes
Enter your product name:Lemon
do you wanna continue yes/no:yes
Enter your product name:Carrot
do you wanna continue yes/no:no
 Thanks For Shopping


    



      
      
      
    
