#both strings should be equal length
#both strings should have same characters in same order or different order
#ABC
#BAC #len=3,characters are also same the these two are anagram
s=input("enter string 1")
s2=input("enter string 2")
if len(s)!=len(s2):
    print(" not anagrams")
else:
    if sorted(s)==sorted(s2):
        print("strings are anagrams")
    else:
        print("not anagrams")