num=int(input("enter a number: "))
result=0
while(num>0):
    lastdigit=num%10
    result=result+lastdigit*lastdigit
    num=num//10
print("sum of square of digits are =",result)