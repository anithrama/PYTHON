class bank:
    def __init__(self,accno,name,balance):
        self.accno=accno
        self.name=name
        self.balance=balance
       
    
    def deposit(self):
        amt=int(input("enter amt:"))
        self.balance+=amt
        print(self.balance,"is balance")
      
    def withdraw(self):
        amt=int(input("enter amt to withdraw:"))
        self.balance-=amt
        print(self.balance,"is balance")
     
name=(input("enter name:"))
accno=(input("enter accno:"))
balance=int(input("enter set balance:"))
b1=bank(name,accno,balance)
b1.deposit()
b1.withdraw()