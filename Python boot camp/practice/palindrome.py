no=int(input("enter number:"))
temp=no
rev=0
while no>0:
    digit=no%10
    rev=rev*10+digit
    no=no//10
if(temp==rev):
    print("is a palindrome")
else:
    print("not a palindrome")
    
