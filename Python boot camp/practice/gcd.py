n1=int(input("enter the number"))
n2=int(input("enter number 2"))
if(n1<n2):
    small=n1
else:
    small=n2
for i in range(1,small+1):
    if n1%i==0 and n2%i==0:
        gcd=i
print(gcd)
