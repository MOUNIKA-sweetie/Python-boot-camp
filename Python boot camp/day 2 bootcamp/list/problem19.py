#you are given with a comma seperated natural numbers 1to 10 print only the even numbers 
my_list=list(map(int,input().split(",")))
count=0
for i in range(1,len(my_list),2):
   #print(my_list[i])
   #print(i)
   count+=1
   print(count)

