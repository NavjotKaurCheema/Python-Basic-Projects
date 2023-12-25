from tkinter import *

def click(text):
    global scvalue
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value="Error!"

        scvalue.set(value)
        screen.update()
       
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()

root.geometry("480x900")
root.title("Navjot's Calculator")
root.wm_iconbitmap()

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="arial 40 bold", bd=10, relief="ridge")
screen.pack(fill=X, ipadx=7, pady=12, padx=12)

buttons = [
    "9", "8", "7",
    "6", "5", "4",
    "3", "2", "1",
    "0", "-", "+",
    "*", "%", "/",
    ".", "C", "="
]

for i in range(0, len(buttons), 3):
    f = Frame(root, bg="lightgrey")
    for j in range(3):
        button_text = buttons[i + j]
        if button_text == "C":
            b = Button(f, text=button_text, padx=28, pady=5, font="arial 25 bold", command=lambda text=button_text: click(text), bg="red", bd=8, relief="ridge", fg="white")
        else:
            b = Button(f, text=button_text, padx=28, pady=5, font="arial 25 bold", command=lambda text=button_text: click(text), bg="lightblue", bd=8, relief="ridge")
        b.pack(side=LEFT, padx=18, pady=12)
    f.pack()

root.mainloop()
