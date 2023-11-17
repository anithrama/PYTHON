# class calc:
#     def __init__(self,a,b):
#         self.n=a
#         self.m=b
#     def add(self):
#         self.sum=self.n+self.m
#         print(self.sum)
#     def sub(self):
#         self.subs=self.n-self.m
#         print(self.subs)
#     def div(self):
#         self.div=self.n/self.m
#         print(self.div)

# k=int(input("enter 1:"))
# p=int(input("enter2:"))
# ob=calc(k,p)
# ob.add()
# ob.sub()
# ob.div()
# t1=int(input("enter 3:"))
# t2=int(input("enter 4:"))
# ob=calc(t1,t2)
# ob.add()
# ob.sub()
# ob.div()





# class bank:
    
#     def __init__(self,name,num,balance):
#         self.name=name
#         self.num=num
#         self.balance=balance
#     def deposit(self):
#         amt=int(input("enter amt:"))
#         self.balance+=amt
#         # print(self.balance,"is balance")
      
#     def withdraw(self):
#         amt=int(input("enter amt to withdraw:"))
#         self.balance-=amt
#         # print(self.balance,"is balance")
#     # print("")
#     def show_balance(self):
#         print("name:",self.name,'\n',"accno:",self.num,'\n',"balance:",self.balance)
# l=[]   
# def create():
#     name=input("enter the name:")
#     accno=int(input("enter the accno:"))
#     balance=int(input("enter the balance:"))
#     x=bank(name,accno,balance)
#     l.append(x)
# while True:
#     print("1.create account\n,2.deposit\n,3.withdraw\n,4,exit\n")
#     ch=int(input("enter the choice:"))
#     if ch==1:
#         create()
#     elif ch==2:
#         ac=int(input("enter ac number:"))
#         for i in l:
#             if ac ==i.num:
#                 i.deposit()
#                 i.show_balance()
#     elif ch==3:
#         ac=int(input("enter ac number:"))
#         for i in l:
#             if ac ==i.num:
#                 i.withdraw()
#                 i.show_balance()
#     elif ch==4:
#         print("invalid")
#         break    

    


# class circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         area=((3.14)*(self.radius)**2)
#         print("radius of the circle:",area)
#     def circumferance(self):
#         c=((2)*(3.14)*(self.radius))
#         print("circumferance of the circle:",c)
     

# area=int(input("enter the radius of the circle:"))
# ci=circle(area)
# while True:
#     print("1.area\n 2.circumferance\n 3.exit\n")
#     choice=int(input("enter the choice:")) 
#     if choice ==1:
#         ci.area()
#     elif choice ==2:
#         ci.circumferance()
#     elif choice ==3:
#         break
#     else:
#         print("invalid")

        
        
    

    
class students:
    
    def __init__(self,name,roll_no):
        self.name=name
        self.roll=roll_no
    
    def display(self):
        print(" name of the student:")
        print(" age of the stdent:")
        

    def setage(self):
        age=int(input("enter the age of the student:"))
        
        
       
    def set_marks(self):
        mark=int(input("enter the mark"))
        self.mark=mark
l=[]   
def create():
    name=input("enter the name:")
    rollno=int(input("enter the rollno:"))
    age=int(input("enter the age:"))
    x=students(name,rollno,age)
    l.append(x)
while True:
    print("1.create students details\n,2.age\n,3.mark\n,4,exit\n")
    ch=int(input("enter the choice:"))
    if ch==1:
        create()
    elif ch==2:
        age()
    elif ch==3:
        mark()
    elif ch==4:
        print("invalid")
        break    



     






















