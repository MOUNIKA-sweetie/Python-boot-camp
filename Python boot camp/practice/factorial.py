n=int(input("enter a number"))
f=1
if(n<0):
 print("no factorial for negative numbers")
elif n==0:
 print("the factorial of 0 is 1")
else:
  for i in range(1,n+1):
   f=f*i
  print(f)

