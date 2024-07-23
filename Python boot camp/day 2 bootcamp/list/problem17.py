b=my_list=list(map(int,input().split(" ")))
print("enter your choice 1.append() 2.pop 3.sort 4.print good morning 5.length()")
choice=int(input())
if(choice==1):
  my_list.append(12)
if(choice==2):
  my_list.pop(1)
if(choice==3):
  my_list.sort()
if(choice==4):
 print("good morning ")
else:
 len(my_list)
 print(my_list)