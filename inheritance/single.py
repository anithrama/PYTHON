# class animal:
#     def speak(self):
#         print("Animal Speaking")
# class lion(animal):
#     def roar(self):
#         print("Lion Roaring")
# d=lion()
# d.roar()
# d.speak()




# class calculation1:
#     def addition(self,x,y):
#         return x+y
# class calculation2:
#     def multiplication(self,x,y):
#         return x*y
# class derived(calculation1,calculation2):
#     def division(self,a,b):
#         return a/b
# d=derived()
# print(d.addition(2,4))
# print(d.multiplication(2,4))
# print(d.division(2,4))



# class animal:
#     def speak(self):
#         print("Animal Speaking")
# class lion(animal):
#     def roar(self):
#         print("Lion Roaring")
# class babylion(lion):
#     def eat(self):
#         print("eating meat...")
# d=babylion()
# d.roar()
# d.speak()
# d.eat()

    
    
# class shape:
#     def __init__(self,area):
#         self.a=area
#     def area(self):
#         print(self.a)
# class rectangle(shape):
#     def area_rectangle(self,l,b):
#         self.a=l*b
#         super().area()
# class circle(shape):
#     def area_circle(self,r):
#         self.a= 3.14*r**2
#         super().area()
# d=circle(0)
# c=rectangle(0)
# c.area_rectangle(2,4)
# d.area_circle(4)



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













    