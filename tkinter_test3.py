from tkinter import *
from tkinter import ttk

def button_click():
    show_selection()
    
def listbox_selected(event):
    #show_selection()
    pass
    
def show_selection():
    for i in lb.curselection():
        print(lb.get(i))

if __name__ == '__main__':
    root = Tk()
    root.title('Listbox 1')
    
    # フレーム
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()
    
    # リストボックス
    currencies = ('JPY', 'USD')
    v1 = StringVar(value=currencies)
    lb = Listbox(frame1, listvariable=v1,height=4)
    lb.insert(END, 'EUR')
    lb.insert(END, 'CHF')
    lb.bind('<<ListboxSelect>>', listbox_selected)
    lb.grid(row=0, column=0)
    
    #Button
    button1 = ttk.Button(frame1, text='OK', command=button_click)
    button1.grid(row=0, column=1)
    
    root.mainloop()