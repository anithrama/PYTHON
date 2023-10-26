l1=[1,2,3,4,5]
l2=[-2,3,4,5,6,7]
l3=[]
i=0
while i<len(l1):
    if l1[i] in l2:
        l3.append(l1[i])
    i=i+1
print(l3)