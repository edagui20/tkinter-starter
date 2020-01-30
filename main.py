

from tkinter import * 
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import Menu
window = Tk()         


window.title("Blue")
lbl = Label(window, text="Fun", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
lbl = Label(window, text="Game", font=("Arial Bold", 20))
lbl.grid(column=0, row=2)
txt= Entry(window,width=20)
txt.grid(column=5, row=0)
txt= Entry(window,width=20)
txt.grid(column=5, row=2)
chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text='Cool', var=chk_state)
chk.grid(column=0, row=4)
chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text='Not Cool', var=chk_state)
chk.grid(column=0, row=5)
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black')
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
bar['value']=70
bar.grid(column=3, row=7)
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='new')
new_item.add_separator()
new_item.add_command(label='Edit')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)
def clicked():
    lbl.configure(text="A virus has been intalled")
btn = Button(window, text="Click to install", command=clicked)
btn.grid(column=1, row=0)
def clicked():
    lbl.configure(text="Installing Virus")
btn = Button(window, text="Click to get a virus", command=clicked)
btn.grid(column=1, row=2)
window.mainloop()     
