#10 apples(15rps) , 24bananas(4rps), 8 orange(5rps)
f1=int(input("enter the no of apples"))
f2=int(input("enter the no of bananas"))
f3=int(input("enter the no of orange"))
x=int(input("how much money mom gave"))
c1=int(input("cost of apple"))
c2=int(input("cost of banana"))
c3=int(input("cost of orange"))
ts=f1*c1+f2*c2+f3*c3
y=int(input("how much shopkeeper gave you"))
if(ts==y):
    print("you are not cheated")
elif(ts!=y):
  print("you are cheated")
