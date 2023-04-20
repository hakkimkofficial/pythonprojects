from tkinter import *
root=Tk()
f=Frame(root)
f.pack()
def fun():
    print('hai avodha')
def cancel():
    print('its cancelled')
Button(f,text='login',bg='red',command=fun).pack()
Button(f,text='cancel',bg='green',command=cancel).pack()

root.mainloop()
