from tkinter import *
w=Tk()
w.title("gui")
w.geometry('450x450')

l1=Label(text='radius')
l1.grid(row=0,column=0)

e1=Entry()
e1.grid(row=0,column=1)

l2=Label(text='answer')
l2.grid(row=1,column=0)

e2=Entry()
e2.grid(row=1,column=1,pady=10)



def area():
        n=int(e1.get())
        area=((3.14)*(n)**2)
        # print("radius of the circle:",area)
        e2.delete(0,END)
        e2.insert(END,area)

b1=Button(text='area of the circle',command=area)
b1.grid(row=2,column=0,pady=10)
w.mainloop()



