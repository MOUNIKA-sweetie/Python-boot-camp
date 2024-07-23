l=int(input("enter the value of n: "))
numbers=[]

index=0
while index<l:
  temp=int(input("enter a number: "))
  numbers.append(temp)
  index+=1
lar=numbers[0]
idex=0
while index<l:
  if numbers[index]>lar:
    lar=numbers[index]
index+=1
print("largest among n numbers is: ",l)  