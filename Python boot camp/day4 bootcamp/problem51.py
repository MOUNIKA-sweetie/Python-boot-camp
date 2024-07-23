a=int(input("enter first number: "))
b=int(input("enter second number: "))
c,d=a,b
while b!=0:
    a,b=b,a%b
    print((c*d)//a)
 
    