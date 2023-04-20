# from tkinter import *
# root=Tk()
# class demo:
#     def __int__(self,rootone):
#         f=Frame(rootone)
#         f.pack()
#         self.p= Button(f,text='hello avodha',command=self.printmsg)
#         self.p.pack()
#         Button(f,text='exit',command=f.quit).pack()
#     def printmsg(self):
#         print('hello am avodha')
# obj=demo(root)
# root.mainloop()
from tkinter import *
root=Tk()
class demo:
    def __init__(self,rootone):
        f=Frame(rootone)
        f.pack()
        self.p=Button(f,text='login',bg='red',command=self.printmsg)
        self.p.pack()
        Button(f,text='exit',bg='green',command=f.quit).pack()
    def printmsg(self):
        print('hello am avodha')
obj=demo(root)
root.mainloop()
