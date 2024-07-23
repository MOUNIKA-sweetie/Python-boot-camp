#LCM and HCF relation between them
a=int(input("enter first number: "))
b=int(input("enter second number: "))
while b!=0:
    a,b=b,a%b
    print("GCD of 2 numbers is:",a)