class calc:
    def __init__(self,a,b):
        self.n=a
        self.m=b
    def add(self):
        self.sum=self.n+self.m
        print(self.sum)
    def sub(self):
        self.subs=self.n-self.m
        print(self.subs)
    def div(self):
        self.div=self.n/self.m
        print(self.div)

k=int(input("enter 1:"))
p=int(input("enter2:"))
ob=calc(k,p)
ob.add()
ob.sub()
ob.div()
t1=int(input("enter 3:"))
t2=int(input("enter 4:"))
ob=calc(t1,t2)
ob.add()
ob.sub()
ob.div()
