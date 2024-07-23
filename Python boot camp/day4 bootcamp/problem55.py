import math
a=int(input("enter a number:"))
r=a**0.5
count=0
for i in range(2,int(r+1)):
    if a%i==0:
        count+=1
        break
if count==0:
      print("prime number")
else:
       print("not a prime")

#import math
#a=int(input("enter a number"))
#flag=False
#for i in range(2,int.(math.sqrt(n)+1))
#if(n%i==0):
 #   flag=True
#if flag=alse:
 #   print("prime")
#else:
 #   print("not a prime")