from menupro import *
from 

from exp3 import *

c=Car()
c.start_engine
# class Employee:
#     def __init__(self,salary):
#         self.a=salary
#     def calculate_salary(self):
#         print("total salary:",self.a)
# class manager(Employee):
#     def calculate_salary(self):
#         da=1000
#         ta=900
#         basic_salary=155000
#         bonus=500
#         self.a=da+ta+basic_salary+bonus
#         self


class employee:
    def __init__(self,salary):
        
        self.s=salary
    def salary(self):
        print(self.s)    

class manager(employee):
    def manager_salary(self,da,ta,bonus,basic_salary):
        # basic_salary=100000
        # ta=5000
        # da=1000
        
        self.s =da+ta+bonus+basic_salary
        super().salary()
class developer(employee):
    def developer_salary(self,da,ta,bonus,basic_salary):
        # basic_salary=50000
        # da=500
        # ta=2500
        
        self.s= da+ta+bonus+basic_salary
        super().salary()
sa=0
m=manager(sa)
d=developer(sa)
m.manager_salary(1000,200,20000,100000)
d.developer_salary(500,100,10000,50000)
