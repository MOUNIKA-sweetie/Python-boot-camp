#find the maximum element in the given list
#my_list=list(map(int,input().split(" ")))
#print(max(my_list))
my_list=list(map(int,input().split(" ")))
max=my_list[0]
for i in range(len(my_list)):
        if(my_list[i]>max):
                max=my_list[i]
print(max)