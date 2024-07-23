#same spelled backward
#madam
#compare last and 1st,last 2nd and 2nd letter
import math
word=input("enter word")
IsitPalindrome = 0 #we are putting zero because we have no data yet
mid = (math.floor(len(word) /2))     
#we are going to find middle letter of our word by usin math.floor
#math.floor function it rounds the number down to the nearest one
#inside of the floor fn we will divide the length/2 ti fnd middle
for i in range(0, mid):
    if(word[i] != word [(len(word) - 1 - i)]):
        IsitPalindrome = 1
if IsitPalindrome == 1:
    print("it is not a palindrome")
else:
    print("it is a palindrome!")           