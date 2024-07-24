n=int(input())
for i in range(n):
    for j in range(i):
        print(' ',end='')
    for m in range(n):
        print('*',end='')
    print()