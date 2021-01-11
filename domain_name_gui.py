import tkinter as tk
from tkinter.messagebox import *
import whois

root = tk.Tk()

def check_availability():
    url = e.get()
    if url != '':
        if '.com' not in url:
            url =  url+'.com'   
        try:
            res = whois.whois(url)
            for x in res.domain_name:
                if x == url.upper():
                    showinfo('Sorry','Domain Name is Taken!\nPlease Try A Different One')
                    e.delete(0,tk.END)
                    break           
        except whois.parser.PywhoisError:
            showinfo('Available!',f'Domain {url} is Available!\nThanks For using Our Service')
            e.delete(0,tk.END)
    else:
        showerror('No Name!','Please Enter a Domain to Check')


root.title('Domain Name Availability Checker')
root.geometry('500x300+500+300')
bg = tk.PhotoImage(file='domain_bg.png')
bg_label = tk.Label(root,image=bg)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)

title = tk.Label(root,text='Enter Domain Name to Check',font=('Gouly old style',20,'bold'),bg='#75c3cf',fg='#000000')
title.place(x=60,y=25)

e = tk.Entry(root,font=('times new roman',15),bg='#FFFFFF',fg='#000000')
e.place(x=70,y=95,width=350,height=35)

checker = tk.Button(root,text='Check',command=check_availability,font=('Gouly old style',20,'bold'),bg='#75c3cf',fg='#000000',relief=tk.RAISED)
checker.place(x=195,y=135)


root.mainloop()
