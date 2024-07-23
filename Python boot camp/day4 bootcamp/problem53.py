#password verifier
#mr x is trying to create a new password for his instagram account these are the required conditions for creating a new password 
#1:minimum length is 8 max 15
#2:only @,# is allowed in a password
#3:no spaces are allowed
#4:only alpha numerics are allowed
#you are supposed to print weak if length is exact 8-12 ,strong if length is b/w 12-15

x=input("enter the password: ")
n=len(x)
a="@","#"
if(n<=8 and a != x):
  print("weak",end=" ")
elif(8<n<15 and a in x ):
  print("strong",end=" ")
