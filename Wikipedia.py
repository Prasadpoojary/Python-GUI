#When you search for something it will give you Wikipedia for your search. NOTE: You must have internet connection.
#to install tkinter 'pip install tkinter'

#import all the required modules
from tkinter import *
import wikipedia
from tkinter import messagebox
from tkinter import filedialog

# function will called when the search button clicked.
def search():
    global result
    text1.delete(0.0,END)
    item=ent1.get()
    result=wikipedia.summary(item)
    text1.insert(INSERT,result)
    
# function will called when the exit button clicked.
def exitmsg():
    q=messagebox.askyesno("Exit","Do you want to Exit from this Search Box?")
    if q is True:
        window.destroy()
# function will called when the clear button clicked.
def clear():
    ent1.delete(0,END)
    text1.delete(0.0,END)
    
# function will called when the save button clicked and save your search result in specified file.
def savefile():
    global result
    f=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    f.write(result)
    f.close()
# initialize Tk to user defined variable window as object.
window=Tk()

# user interface designs.
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

#end of window object
window.mainloop()
