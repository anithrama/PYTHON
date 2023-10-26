sum=0
list=[]
num=int(input("enter no:of elements:"))
i=1
while i<=num:
    p=int(input("enter the no"))
    list.append(p)
    print(list)
    sum+=p
    i=i+1
print(list,sum) 
