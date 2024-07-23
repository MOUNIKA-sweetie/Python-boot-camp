#s=input()
#vowels="aeiouAEIOU"
#count=0
#for char in s:
#    if char not in vowels:
 #       count+=1
#print(count)
vowel="aeiou"
consonet="bcdfghjklmnpqrstvwxyz"
count=0
c=0
i="hello world"
inp=i.lower()
for i in inp:
    if (i in consonet):
        count+=1
print(count)