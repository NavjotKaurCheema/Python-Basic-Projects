from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip

def generator():
    if choice.get() not in [1, 2, 3]:
        messagebox.showerror("Error", "Please select a password strength level.")
        return

    s_alpha = string.ascii_lowercase
    l_alpha = string.ascii_uppercase
    num = string.digits
    special_char = string.punctuation

    all_chars = s_alpha + l_alpha + num + special_char
    pass_length = int(max_length.get())

    password = ""

    if choice.get() == 1:
        password = ''.join(random.sample(s_alpha, pass_length))
    elif choice.get() == 2:
        password = ''.join(random.sample(s_alpha + l_alpha, pass_length))
    elif choice.get() == 3:
        password = ''.join(random.sample(all_chars, pass_length))

    # Clear existing content and insert the new password
    reqpass.delete(0, END)
    reqpass.insert(0, password)

def copy():
    r_password = reqpass.get()
    pyperclip.copy(r_password)

wd = Tk()
wd.config(bg='#800000')
choice = IntVar()
Font = ('times new roman', 13, 'bold')
passwordLabel = Label(wd, text='***PA$$WORD GENERATOR***', font=('montserrat', 18, 'bold'), bg='#800000', fg='white')
passwordLabel.grid(pady=20)

wrButton = Radiobutton(wd, text='Weak', value=1, variable=choice, font=Font)
wrButton.grid(pady=15)

mrButton = Radiobutton(wd, text='Medium', value=2, variable=choice, font=Font)
mrButton.grid(pady=15)

srButton = Radiobutton(wd, text='Strong', value=3, variable=choice, font=Font)
srButton.grid(pady=15)

LengthLabel = Label(wd, text='Password Length (4-20)', font=('cambria', 14, 'bold'), bg='#800000', fg='white')
LengthLabel.grid(pady=2)

max_length = Spinbox(wd, from_=4, to_=20, font=Font)
max_length.grid(pady=15)

genButton = Button(wd, text="Generate", font=Font, command=generator)
genButton.grid(pady=2)

reqpass = Entry(wd, width=30, bd=2, font=Font)
reqpass.grid(pady=15)

copyButton = Button(wd, text="Copy", font=Font, command=copy)
copyButton.grid(pady=15)

wd.mainloop()
