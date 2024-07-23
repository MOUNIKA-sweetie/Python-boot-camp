#replace the elements in the array with avg of max and min element 
my_list=list(map(int,input().split(" ")))
max=my_list[0]
for i in range(len(my_list)):
        if(my_list[i]>max):
                max=my_list[i]
print(max)
min=my_list[0]
for i in range(len(my_list)):
        if(my_list[i]<min):
                min=my_list[i]
print(min)

sum=min+max
avg=sum//2#it will convert into float
print(avg)
for i in range(len(my_list)):
 my_list[i]=avg
print(my_list)
