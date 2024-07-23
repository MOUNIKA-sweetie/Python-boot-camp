# input:hello---wrd---ld
# --------hello world
n=input()
n2=""
count=0
for i in n:
    if(i=="-"):
        count+=1
    else:
        n2=n2+i
print('_'*count+n2)