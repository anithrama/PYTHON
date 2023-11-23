# from tkinter import *
# w=Tk()
# w.geometry('350x350')
# l1=Label(text='name:')
# l1.grid(row=0,column=0)

# e1=Entry()
# e1.grid(row=0,column=1)

# l2=Label(text='password:')
# l2.grid(row=1,column=0)
# e2=Entry()
# e2.grid(row=1,column=1,pady=15)
# w.mainloop()



# from tkinter import *
# w=Tk()
# w.geometry('350x350')
# l1=Label(text='name:')
# l1.place(x=10,y=10)
# e1=Entry()
# e1.place(x=55,y=10)
# w.mainloop()


import tkinter
from tkinter import *
from PIL import Image, ImageTk
root =Tk()
root.geometry('500x500')
Image1 =Image.open("313.jpeg")
test = ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.images =test
label1.pack()
root.mainloop()
