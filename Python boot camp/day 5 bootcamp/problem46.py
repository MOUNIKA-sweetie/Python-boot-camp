#print the unique characters in a string
vowel="aeiou"
consonet="bcdfghjklmnpqrstvwxyz"
count=0
ans=""
i="hello world"
inp=i.lower()
for i in inp:
   if(i not in ans):
     ans+=i
print(ans)