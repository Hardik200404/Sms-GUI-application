import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
root=tk.Tk()
root.geometry('600x400')
root.maxsize(600,400)
root.minsize(600,400)
root.title('send message')
root.wm_iconbitmap('Sms-B.ico')

def send_sms():
    number=phone_no.get()
    messages=message.get("1.0","end-1c")
    #initializing url and api key
    url="https://www.fast2sms.com/dev/bulk"
    api="7kLrY8CuJAE3G5h2jSzOgV0Ib9UDqasKypRXQ4FWT6PfcBxvodoDkxyN9ZhCPaXHfcUn5GMBRTtl4gz0"
    querystring={
                 "authorization":api,
                 "sender_id":"FSTSMS",
                 "message":messages,
                 "language":"english",
                 "route":"p",
                 "numbers":number   }
    headers={'cache-control':"no-cache"}

    requests.request("GET",url,headers=headers,params=querystring)
    messagebox.showinfo("Send SMS",'SMS has been send successfully')

img=ImageTk.PhotoImage(Image.open('images.jpg'))#Background
panel=Label(root,image=img)
panel.pack(side="bottom",fill="both",expand="yes")
lable=Label(root,text="Send SMS Using Python",font=('verdana',10,'bold'))
lable.place(x=210,y=10)
phone_no=Entry(root,width=20,borderwidth=0,font=('verdana',10,'bold'))
phone_no.place(x=220,y=115)
phone_no.insert('end','phone number')
message=Text(root,height=5,width=25,borderwidth=0,font=('verdana',10,'bold'))
message.place(x=190,y=140)
message.insert('end','Message')
send=Button(root,text="Send Message",font=('verdana',10,'bold'),relief=RIDGE,cursor='hand2',borderwidth=0,command=send_sms)
send.place(x=260,y=235)
root.mainloop()            
            
            
            
            
            
            
            
            