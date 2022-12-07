from twilio.rest import Client
from tkinter import messagebox
import tkinter as tk
import random
import time
otp=random.randint(999,10000)
otp=str(otp)




def check():
    userentry = y.get()
    if otp == userentry:
        messagebox.showinfo("showinfo","Login success")
    else:
        messagebox.showinfo("showinfo","Invalid")


def timelimit():
    start = time.time()
    global elapsed
    elapsed = 0
    while elapsed < 10:
        elapsed = time.time() - start



def sendsms():
    number=x.get()
    client = Client('', '')
    client.messages.create(from_='+17739005527 ', to=number, body="your otp is: " + otp)
    messagebox.showinfo("showinfo","otp sent ...")
    root.destroy()
    win=tk.Tk()
    win.geometry("300x200")
    global y
    y = tk.StringVar()
    l1 = tk.Label(win, text="Enter OTP")
    l1.place(x=10, y=5)
    e1 = tk.Entry(win,textvariable=y)
    e1.place(x=10, y=30, height=30, width=250)
    b1 = tk.Button(win, text="Submit", fg="red", bg="yellow", command=check)
    b1.place(x=10, y=70)


root=tk.Tk()
root.geometry('300x200')
root.title("OTP Verification")
x=tk.StringVar()
l=tk.Label(root,text="Enter your number with country code")
l.place(x=10,y=5)
e=tk.Entry(root,textvariable=x)
e.place(x=10,y=30,height=30,width=250)
b=tk.Button(root,text="Send Otp",fg="red",bg="yellow",command=sendsms)
b.place(x=10,y=70)

root.mainloop()
