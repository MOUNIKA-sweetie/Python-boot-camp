#any positive integer of n digits is armstrong number
#if the sum of the nth power of each digits equals to the number itself
#123=1*1*1+2*2*2+3*3*3
num=int(input("enter any positive number"))
#l=len(str(num))
#print(l)
x=num
y=num
count=0
while num>0:
    r=num%10
    count=count+1
    num=num//10
    sum=0
while x>0:
    r=x%10
    sum=sum+(r**count)
    x=x//10

if sum==y:
    print(y,"is an armstrong number")
else:
    print(y,"is not an armstrong ")