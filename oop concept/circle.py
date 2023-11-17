class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=((3.14)*(self.radius)**2)
        print("radius of the circle:",area)
    def circumferance(self):
        c=((2)*(3.14)*(self.radius))
        print("circumferance of the circle:",c)
     

area=int(input("enter the radius of the circle:"))
ci=circle(area)
while True:
    print("1.area\n 2.circumferance\n 3.exit\n")
    choice=int(input("enter the choice:")) 
    if choice ==1:
        ci.area()
    elif choice ==2:
        ci.circumferance()
    elif choice ==3:
        break
    else:
        print("invalid")
