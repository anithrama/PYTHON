string=(input("enter a line:"))
count=1
i=0
while i<len(string):
    if string[i].isalpha():
        pass
    else:
        count+=1
    i=i+1
print(count)
