
#logical operator
age=int(input("enter your age"))
if(age>=18 and age<=24):
    print("only two wheerler")
elif(age>24 and age<=45):
    print("two and four wheeler")
elif(age<18):
    print("not eligible")
else:
    print("ALL")