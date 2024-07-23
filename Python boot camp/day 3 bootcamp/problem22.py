#find the element that is present in k+n index
#step1:list input
#input of k
#input of n
#for loop

#k=3
#n=2
#3,6,8,4,61,2 the input values
my_list=list(map(int,input().split(" ")))
k=int(input())
n=int(input())
l=len(my_list)
    #if(k<=n):
        #print(my_list[i])
if(k+n<l):
        print("error")
else:
    for i in range(k,len(my_list)):
        print((my_list[k+n]))
        
 
 


