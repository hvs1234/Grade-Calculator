#Libraries
from tkinter import *
from tkinter import messagebox

#Application Setup
root = Tk()
root.resizable(False,False)
root.configure(bg="slate blue")
root.geometry("500x400+380+180")
root.title("Grade Calculator")

#Functions
def calculate():
    e1 = int(Eentry.get())
    c1 = int(Centry.get())
    g1 = int(Gentry.get())
    if(e1=="" and c1=="" and g1==""):
        messagebox.showwarning("Blank Input","Please enter some value!")
    total = (e1+c1+g1)
    Label(text=f"{total}",font="arial 15 bold",bg="slate blue",fg="orange").place(x=250,y=170)
    avg = int(total/3)
    Label(text=f"{avg}",font="arial 15 bold",bg="slate blue",fg="yellow").place(x=250,y=210)
    if(avg>50):
        grade = "Pass"
        if(grade=="Pass"):
            Label(text=f"{grade}",font="arial 15 bold",bg="slate blue",fg="lime").place(x=250,y=270)
    else:
        grade = "Fail"
        Label(text=f"{grade}",font="arial 15 bold",bg="slate blue",fg="red").place(x=250,y=270)

#Application Creation
img1 = PhotoImage(file="E:\\pyImages\\grade logo.png")
root.iconphoto(False,img1)

sub1 = Label(root,text="English: ",font="Monospace 10 bold",bg="slate blue",fg="black")
sub1.place(x=50,y=20)

sub2 = Label(root,text="Computer Science: ",font="Monospace 10 bold",bg="slate blue",fg="black")
sub2.place(x=50,y=70)

sub3 = Label(root,text="General Knowledge: ",font="Monospace 10 bold",bg="slate blue",fg="black")
sub3.place(x=50,y=120)

total = Label(root,text="Total: ",font="Monospace 10 bold",bg="slate blue",fg="black")
total.place(x=50,y=170)

average = Label(root,text="Average: ",font="Monospace 10 bold",bg="slate blue",fg="black")
average.place(x=50,y=220)

grade = Label(root,text="Grade: ",font="Monospace 10 bold",bg="slate blue",fg="black")
grade.place(x=50,y=270)

Evalue = StringVar()
Cvalue = StringVar()
Gvalue = StringVar()

Eentry = Entry(root,textvariable=Evalue,bd=4,width=15,font="Arial 15 bold",fg="indigo",bg="light grey")
Eentry.place(x=250,y=20)
Centry = Entry(root,textvariable=Cvalue,bd=4,width=15,font="Arial 15 bold",fg="indigo",bg="light grey")
Centry.place(x=250,y=70)
Gentry = Entry(root,textvariable=Gvalue,bd=4,width=15,font="Arial 15 bold",fg="indigo",bg="light grey")
Gentry.place(x=250,y=120)

btn1 = Button(root,text="Calculate",font="Monospace 15 bold",fg="black",activeforeground="black",
            bg="slate blue",activebackground="slate blue",bd=4,width=10,command=lambda: calculate())
btn1.place(x=50,y=320)
btn2 = Button(root,text="Exit",font="Monospace 15 bold",fg="black",activeforeground="black",
            bg="slate blue",activebackground="slate blue",bd=4,width=10,command=lambda: root.destroy())
btn2.place(x=250,y=320)
root.mainloop()
