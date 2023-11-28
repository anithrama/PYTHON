from tkinter import *
w=Tk()
w.title("gui")
w.geometry('250x250')
l1=Label(text='hello world',fg='white',bg='black',font=('arial',20,'bold'))
l1.pack(fill=Y,pady=15)
l2=Label(text='hello world',fg='white',bg='black')
l2.pack(fill=X,pady=15)
w.mainloop()



