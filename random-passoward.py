import tkinter as tk
from tkinter import ttk
import string
import random
window = tk.Tk()
window.title("Passoward Generator")
window.geometry("400x300")

#creating grid
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=1)
window.rowconfigure(2,weight=1)
window.rowconfigure(3,weight=1)
window.rowconfigure(4,weight=1)

#creating output display
displayvar = tk.StringVar()
display = ttk.Entry(window,font=(30),textvariable=displayvar)
display.grid(row=0,column=0,columnspan=2,sticky="ewns",padx=10,pady=10)

#creating function
s_var = tk.IntVar()
def fun():
    passoward = ""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special_chr = string.punctuation
    all_chr = lower+upper+digits+special_chr
    for i in range (s_var.get()):
        passoward += random.choice(all_chr)
    displayvar.set(passoward)




#creating button
b8 = ttk.Button(window,text="passoward length = 8",command=lambda:s_var.set(8))
b12 = ttk.Button(window,text="passoward length = 12",command=lambda:s_var.set(12))
b16 = ttk.Button(window,text="passoward length = 16",command=lambda:s_var.set(16))
b24 = ttk.Button(window,text="passoward length = 24",command=lambda:s_var.set(24))
b32 = ttk.Button(window,text="passoward length = 32",command=lambda:s_var.set(32))
b64 = ttk.Button(window,text="passoward length = 64",command=lambda:s_var.set(64))

b8.grid(row=1,column=0,sticky="ewns")
b12.grid(row=1,column=1,sticky="ewns")
b16.grid(row=2,column=0,sticky="ewns")
b24.grid(row=2,column=1,sticky="ewns")
b32.grid(row=3,column=0,sticky="ewns")
b64.grid(row=3,column=1,sticky="ewns")

start_button = ttk.Button(window,text="GENERATE",command= fun)
start_button.grid(row=4,column=1,sticky="ewns",padx=10,pady=10)
clear_button = ttk.Button(window,text="CLEAR",command=lambda:displayvar.set(""))
clear_button.grid(row=4,column=0,sticky="ewns",padx=10,pady=10)






window.mainloop()