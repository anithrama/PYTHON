s={}
string=input("enter a string:")
i=0
while i<len(string):
    if string[i] in s:
        s[string[i]]+=1
    else:
        s[string[i]]=1
    i=i+1
print(s)
    
