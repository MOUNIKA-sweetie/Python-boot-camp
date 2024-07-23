#print all the qowels follwed by consonants
vowel="aeiou"
consonet="bcdfghjklmnpqrstvwxyz"
count=0
ans=""
i="hello world"
inp=i.lower()
for i in inp:
   if(i in vowel):
      ans+=i
print(ans)
for i in inp:
   if(i in consonet):
      ans+=i
print(ans,end=" ") 