#sequence of integers of a number
#formed by the addition of the preceding two number in the series
#it is calculated by addition of two preceding no
n=int(input())
n1,n2=0,1
sum=0
if n<=0:
    print("enter no greater than 0")
else:
    for i in range(0,n):
        print(sum,end=" ")
        n1=n2
        n2=sum
        sum=n1+n2
        