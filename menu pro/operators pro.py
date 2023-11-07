# def add():
#     a=int(input("enter a:"))
#     b=int(input("enter b:"))
#     sum=a+b
#     print(sum)
# def sub():
#     a=int(input("enter a:"))
#     b=int(input("enter b:"))
#     result=a-b
#     print(result)
# def div():
#     a=int(input("enter a:"))
#     b=int(input("enter b:"))
#     result=a/b
#     print(result)
# print("1.add\n 2.sub\n 3.division\n")
# while True:
#     ch=int(input("enter the choice:"))
#     if ch==1:
#         add()
#     elif ch==2:
#         sub()
#     elif ch==3:
#         div()
#     elif ch==4:
#         print("invalid")
#         break
    



# list=["apple,orange,mango,cherry"]

# def add():
#     item=(input("enter item to add:"))
#     list.append(item)
   
# def replace():
#     item=(input("enter position:"))
#     new=input("enter new item:")
#     list.append(item)
    
# def remove():
#     item=(input("enter  item to remove:"))
#     list.append(item)

# def sort() :
#     item=(input("enter item to sort:"))
#     list.append(item)
# def exit():
#     item=(input("enter item to exit:"))
#     list.append(item)
    
# print("1.add\n 2.replace\n 3.remove\n 4.sort\5 5.exit\n")
# while True:
#     ch=int(input("enter the choice:"))
#     if ch==1:
#         add()
#     elif ch==2:
#         replace()
#     elif ch==3:
#         remove() 
#     elif ch==4:
#         sort()
#     elif ch==5:
#         exit()
#     elif ch==6:
#         print("invalid")
#         break
#     print(list)




l=[]
def create():
    n=int(input("enter limit"))
    for i in range(n):
        item=input("enter item:")
        l.append(item)
    print(l)
def add():
    e=input("enter item")
    l.append(e)
    print(l)
def replace():
    n=int(input("enter position:"))
    l.pop(n)
    new=input("enter new item:")
    l .insert(n,new)
    print(l)
def remove():
    item=input("enter item:")
    l.remove(item)
    print(l)
def sort():
    item=input("enter item:")
    l.sort(item)
    print(l)
def exit():
    item=input("enter item:")
    l.exit(item)
    print(l)
print("1.create\n 2.add\n 3.replace\n 4.remove\n 5.sort\5 6.exit\n")
while True:
    ch=int(input("enter the choice:"))
    if ch==1:
        create()
    elif ch==2:
        add()
    elif ch==3:
        replace() 
    elif ch==4:
        remove()
    elif ch==5:
        sort()
    elif ch==6:
        exit()

    elif ch==6:
        print("invalid")
        break
    






    


