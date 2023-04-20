from tkinter import *
import tkinter.messagebox
root=Tk()
#----- message box-----
#showinfo,showwarning,showerror,askquestion,askokcancel,askyesno,askretrycancel
tkinter.messagebox.askretrycancel('title','this is question')
root.mainloop()