from tkinter import *
root=Tk()
def fun():
    print('am function')
mymenu=Menu(root)
root.config(menu=mymenu)
submenu=Menu(mymenu)

mymenu.add_cascade(label='file',menu=submenu)
submenu.add_command(label='save',command=fun)
submenu.add_separator()
submenu.add_command(label='exit',command=root.quit)


newmenu=Menu(mymenu)
mymenu.add_cascade(label='Edit',menu=newmenu)
newmenu.add_command(label='Undo',command=fun)
newmenu.add_command(label='Redo',command=fun)

root.mainloop()