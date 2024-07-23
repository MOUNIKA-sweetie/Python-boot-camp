#find the missing number in an array
#there will be given sequence of numbers
my_list=list(map(int,input().split(" ")))
for i in range(len(my_list)):
    if(my_list[i]+1!=my_list[i+1]):
        print(my_list[i]+1)
        break
    
    
        

        
    

