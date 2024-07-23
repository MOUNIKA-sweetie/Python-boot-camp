list=[2,4,5,6,8,9,10,11,12]
rev_list=[]
print("before reversing:",list)
for i in range(len(list)-1,-1,-1):
    rev_list.append(list[i])
print("after reversing",rev_list)
