#Online Shopping
Z=input("Enter Your Name:")
a=int(input("Enter Your  Login id:"))
b=(input("Enter Your Password:"))
if b.isalpha():
    print("Invalid Password")
    print("Note Password Must be Mix of  Alphabets and Numbers")
    b=(input("Enter Your Password Again:"))

elif b.isnumeric():
    print("Wrong Password")
    print("Note Password Must be Mix of Alphabets and Numbers")
    b=(input("Enter Your Password Again:"))

elif b.isalnum():
    c="WELCOMEBACK".rjust(35," ")
    print(c,Z)

print('''Available Fresh Items Are:
         ____________________________
        |  Item Name  | Price(per kg)|
        |_____________|______________|
        | Rice        |   60         |
        | Tomato      |   35         |
        | Wheat       |   40         |
        | Carrot      |   30         |
        | Chicken     |   200        |
        | Spinach     |   30         |
        | Onion       |   60         |
        | Raddish     |   35         |
        | Mutton      |   720        |
        | Potato      |   30         | 
        |____________________________| 

Note: The Order Should be Minimum of 4 Items''')
w=('''Rice,Tomato,Raddish,Mutton,Potato,Wheat,Carrot,Chicken,Spinach,Onion''')
a=0
b='yes'
z=0
while b=='yes' and a<4:
             c=(input("Enter your product name:"))
             q=c.title()            
             if q in w:
                v=int(input("Enter Your Qty in Kg:"))
                if c=='spinach':
                    p=(print("The cost of",c,"Will be:",v*30))
                    w=v*30
                    z+=w
                    print(w)
                if c=='rice':
                    o=(print("The cost of",c,"Will be:",v*60))
                    x=v*60
                    z+=x
                    print(x)
                elif c=='onion':
                    on=(print("The cost of",c,"Will be:",v*60))
                    k=v*60
                    z+=k
                    print(k)
                elif c=='tomato':
                    to=(print("The cost of",c,"Will be:",v*35))
                    l=v*35
                    z+=l
                    print(l)
                elif c=='wheat':
                    wh=(print("The cost of",c,"Will be:",v*40))
                    m=v*40
                    z+=m
                    print(m)
                elif c=='carrot':
                    ca=(print("The cost of",c,"Will be:",v*30))
                    n=v*30
                    z+=n
                    print(n)
                elif c=='chicken':
                    ch=(print("The cost of",c,"Will be:",v*200))
                    u=v*200
                    z+=u
                    print(u)
                elif c=='raddish':
                    ra=(print("The cost of",c,"Will be:",v*35))
                    pl=v*35
                    z+=pl
                    print(pl)
                elif c=='mutton':
                    mu=(print("The cost of ",c,"Will be:",v*720))
                    qw=v*720
                    z+=qw
                    print(qw)
                elif c=='potato':
                    po=(print("The cost of",c,"Will be:",v*30))
                    we=v*30
                    z+=we
                    print(we)
                    
                a+=1
             else:
                print("Sorry Product Not Available")
d=input("do you wanna continue yes/no:")
q=0
if d=='yes':
   while b=='yes' and q<1:
        c=(input("Enter your product name:"))
        qty=int(input("Enter Your Qty in Kg:"))
        if c=='spinach':
           p=(print("The cost of",c,"Will be:",v*30))
           w=v*30
           z+=w
           print(w)
        if c=='rice':
           o=(print("The cost of",c,"Will be:",v*60))
           x=v*60
           z+=x
           print(x)
        elif c=='onion':
             on=(print("The cost of",c,"Will be:",v*60))
             o=v*60
             z+=o
             print(o)
        elif c=='tomato':
             to=(print("The cost of",c,"Will be:",v*35))
             l=v*35
             z+=l
             print(l)
        elif c=='wheat':
             wh=(print("The cost of",c,"Will be:",v*40))
             m=v*40
             z+=m
             print(m)
        elif c=='carrot':
             ca=(print("The cost of",c,"Will be:",v*30))
             n=v*30
             z+=n
             print(n)
        elif c=='chicken':
             ch=(print("The cost of",c,"Will be:",v*200))
             u=v*200
             z+=u
             print(u)
        elif c=='raddish':
             ra=(print("The cost of",c,"Will be:",v*35))
             pl=v*35
             z+=pl
             print(pl)
        elif c=='mutton':
             mu=(print("The cost of ",c,"Will be:",v*720))
             qw=v*720
             z+=qw
             print(qw)
        elif c=='potato':
             po=(print("The cost of",c,"Will be:",v*30))
             we=v*30
             z+=we
             print(we)
        a+=1
        x=input("do you wanna continue yes/no:")
        if x=='no':
                print("Your items are added to cart")
                print("Your total cost will be:",z)
                break
            
        elif z>250 and z<500:
             dic=10/100*z
             price=z-dic
             print("Congrats you got discount of 10%")
             print("Your final cost will be:",price)
    
        elif z>500 and z<750:
             dic=20/100*z
             price=z-dic
             print("Congrats you got discount of 20%")
             print("Your final cost will be:",price)
    
        elif z>750 and z<1000000:
             dic=30/100*z
             price=z-dic
             print("Congrats you got discount of 30%")
             
             print("your final cost will be:",price)
             

if d=='no':
    print("Your items are added to cart")
    print("Your total cost will be:",z)
    
if z>250 and z<500:
    dic=10/100*z
    price=z-dic
    print("Congrats you got discount of 10%")
    
    print("Your final cost will be:",price)
    
elif z>500 and z<750:
    dic=20/100*z
    price=z-dic
    print("Congrats you got discount of 20%")
    
    print("Your final cost will be:",price)
    
elif z>750 and z<1000000:
    dic=30/100*z
    price=z-dic
    print("Congrats you got discount of 30%")
    
    print("your final cost will be:",price)


'''OUTPUT:

Enter Your Name:Arun Raj L
Enter Your  Login id:9710361338
Enter Your Password:Thanos
Invalid Password
Note Password Must be Mix of  Alphabets and Numbers
Enter Your Password Again:Thanos1234

Available Fresh Items Are:
         ____________________________
        |  Item Name  | Price(per kg)|
        |_____________|______________|
        | Rice        |   60         |
        | Tomato      |   35         |
        | Wheat       |   40         |
        | Carrot      |   30         |
        | Chicken     |   200        |
        | Spinach     |   30         |
        | Onion       |   60         |
        | Raddish     |   35         |
        | Mutton      |   720        |
        | Potato      |   30         | 
        |____________________________| 

Note: The Order Should be Minimum of 4 Items

Enter your product name:chicken
Enter Your Qty in Kg:3
The cost of chicken Will be: 600
600

Enter your product name:rice
Enter Your Qty in Kg:4
The cost of rice Will be: 240
240

Enter your product name:potato
Enter Your Qty in Kg:5
The cost of potato Will be: 150
150

Enter your product name:mutton
Enter Your Qty in Kg:4
The cost of  mutton Will be: 2880
2880

do you wanna continue yes/no:yes

Enter your product name:wheat
Enter Your Qty in Kg:8
The cost of wheat Will be: 160
160

do you wanna continue yes/no:no

Your items are added to cart
Your total cost will be: 4030
Congrats you got discount of 30%:)
your final cost will be: 2821.0'''


    
