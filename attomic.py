from tkinter import *
w=Tk()
w.title("gui")
w.geometry('450x450')
l1=Label(text='number')
l1.grid(row=0,column=0)

e1=Entry()
e1.grid(row=0,column=1)

l2=Label(text='factorial of the number')
l2.grid(row=1,column=0)

e2=Entry()
e2.grid(row=1,column=1,pady=15)

# l3=Label(text='factorial ')
# l3.grid(row=1,column=0)

# e3=Entry()
# e3.grid(row=1 ,column=1)


def factorial():
    n=int(e1.get())
    result =1
    for i in range(1,n+1):
        result *=i
    e2.delete(0,END)
    e2.insert(END,result)

b1=Button(text='factorial of the number',command=factorial)
b1.grid(row=2,column=0,pady=10)
w.mainloop()



