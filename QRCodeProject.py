from tkinter import *
from tkinter import filedialog
import pyqrcode
from pyqrcode import QRCode
from tkinter import messagebox as mb

window=Tk()
window.title("QRCode Generator from Prasad Poojary ")
window.geometry("600x450+350+100")
window.configure(bg="#960018")


def generatebtnclick():
    s=ent1.get()
    if len(s) == 0:
        mb.showwarning("Failed","Please Enter the Link to generate QR Code")
    else:
            qrcode=pyqrcode.create(s)
            f=filedialog.asksaveasfilename()
            m=f[53:]
            qrcode.svg(str(m)+".html",scale=10)
            mb.showinfo("Succuss","QR Code Succussfully Generated")
def generateqr(event):
    s=ent1.get()
    if len(s) == 0:
        mb.showwarning("Failed","Please Enter the Link to generate QR Code")
    else:
            qrcode=pyqrcode.create(s)
            f=filedialog.asksaveasfilename()
            m=f[53:]
            qrcode.svg(str(m)+".html",scale=10)
            mb.showinfo("Succuss","QR Code Succussfully Generated")

 
label1=Label(window,text="QR Code Generator",font="TimesNewRoman 30 bold",bg="#960018",fg="white")
label1.place(x=145,y=100)
label2=Label(window,text="Enter Link : ",font="arial 17",bg="#960018",fg="white")
label2.place(x=50,y=170)
ent1=Entry(window,font="arial 15",bg="white",fg="blue",width="30")
ent1.place(x=180,y=170)
ent1.focus_set()
ent1.bind("<Return>",generateqr)
btn1=Button(window,text="Generate",font="TimesNewRoman 14 bold",bg="white", fg="#960018",command=generatebtnclick)
btn1.place(x=270,y=220)
window.mainloop()

