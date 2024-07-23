#find the duplicates in the array
my_list=list(map(int,input().split(" ")))
new=[]
for i in my_list :
    if(i not in new):
      new.append(i)
      print(*new)