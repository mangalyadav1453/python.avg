print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
print("5. floor division")
print("6. exponentiaation")
print ("7. exit()")
      
i=True
while i==True:
    op= int(input("enter choice(1/2/3/4/5/6/7):"))
    if op==1:
        a=int(input("enter the first number:"))
        b=int(input("enter the second number:"))
        print("addition is:",int(a+b))
    elif op==2:
        a= int(input("enter the first number:"))
        b= int(input("enter the second number:"))
        print("subtraction is:", int(a-b))
    elif op==3:
        a=int(input("enter the first number:"))
        b=int(input("enter the second number:"))
        print("multiplication is:",int (a*b))
    elif op==4:
        a=int(input("enter the first number:"))
        b=int(input("enter the second number:"))
        print("division is:",int(a/b))
    elif op==5:
        a=int(input("enter the first number:"))
        b=int(input("enter the second number:"))
        print("floor division is :",int(a//b))
    elif op==6:
        a=int(input("enter the first number:"))
        b=int(input("enter the second number:"))
        print("exponentation is:",int(a**b))
    elif op==7:
        print("exit the code")
        i=False
    else:
        print("invalid choice")
