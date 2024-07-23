#sort elements in ascending and descending order
my_list=list(map(int,input().split(" ")))
for i in range(0,len(my_list)-1):
 my_list[i]=my_list[i-1]
 print(my_list)