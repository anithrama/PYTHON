# f=open("prgrm1.py",'x')
# f=open("prgrm1.py",'w')
# f.write("x=1""\n""print(x)")

# f=open("prgrm1.py",'a')
# f.write("\n""y=5""\n""print(y)")

# f=open("prgrm1.py",'r')
# print(f.read())
# f.close()

while True:
    ch=(int(input("1.create 2.write 3.append 4.read 5.break \n")))
    if ch==1:
        # n=str(input("enter the file name"))
        f=open("prgrm1.py",'x')
    if ch==2:
        # name=str(input("enter a input:"))
        f=open("prgrm1.py",'w')
        f.write("\n""hello")
        f.close()
    if ch==3:
        # name=str(input("enter a input:"))
        f=open("prgrm1.py",'a')
        f.write("\n""world")
        f.close()
    if ch==4:
        f=open("prgrm1.py",'r')
        print(f.read())
        f.close()
    if ch>=5:
        break

        











