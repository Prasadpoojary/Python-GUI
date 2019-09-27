from tkinter import *
import wikipedia
from tkinter import messagebox
from tkinter import filedialog

def search():
    global result
    text1.delete(0.0,END)
    item=ent1.get()
    result=wikipedia.summary(item)
    text1.insert(INSERT,result)

def exitmsg():
    q=messagebox.askyesno("Exit","Do you want to Exit from this Search Box?")
    if q is True:
        window.destroy()

def clear():
    ent1.delete(0,END)
    text1.delete(0.0,END)

def savefile():
    global result
    f=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    f.write(result)
    f.close()
window=Tk()
window.title("Seach Box")
window.geometry("800x600+250+0")
window.configure(bg="purple")
lab1=Label(window,text="Enter any Word",bg="purple",fg="white",font="none 23 bold")
lab1.place(x=300,y=50)
ent1=Entry(window,width="30",font="none 17 bold")
ent1.place(x=200,y=100)
ent1.focus_set()
btn1=Button(window,text="Search",fg="purple",bg="light grey",font="none 17 bold",command=search)
btn1.place(x=350,y=150)
scroll=Scrollbar(window)
scroll.pack(side=RIGHT,fill=Y)
text1=Text(window,width="69",height="14",font="none 15",wrap="word",yscrollcommand=scroll.set)
text1.place(x=11,y=200)
scroll.config(command=text1.yview)
btn2=Button(window,text="Exit",fg="purple",bg="light grey",font="none 17 bold",width="10",command=exitmsg)
btn2.place(x=11,y=540)
btn3=Button(window,text="Clear",fg="purple",bg="light grey",font="none 17 bold",width="10",command=clear)
btn3.place(x=325,y=540)
btn4=Button(window,text="Save",fg="purple",bg="light grey",font="none 17 bold",width="10",command=savefile)
btn4.place(x=622,y=540)
window.mainloop()
