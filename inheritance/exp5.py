class bankaccount:
    def __init__(self,amounts):
        self.a=amounts
    def deposit(self):
        print()

    def withdraw(self):
        amount=int(input("enter withdraw amount:""\n"))
        
        self.a+=amount
class savinAccount(bankaccount):
    def withdrawl(self):
        super().withdraw()
        limit=50000
        if self.a>limit:
            print("amount exceded than withdrawel limit")
        else:
            print("withdrawal successful")

class checkingaccpunt(bankaccount):
    def withdrawl(self):
        super().withdraw()
        limit=10000
        if self.a>limit:
            print("amount exceded than withdrawel limit")
        else:
            print("withdrawal successful")
while True:
    ch=int(input("1.savingsaac 2.checkingac 3.exit, enter your choice""\n"))
    if ch==1:
        obj=savinAccount(0)
        obj.withdrawl()
    if ch==2:
        obj2=checkingaccpunt(0)
        obj2.withdrawl()

    if ch==3:
        break