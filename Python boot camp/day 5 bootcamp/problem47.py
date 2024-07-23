#count how many vowels are in stri
check=['a','e','i','o','u']
count=0
inp=str(input())
for i in inp:
    if(i in check):
        count+=1
print(count)