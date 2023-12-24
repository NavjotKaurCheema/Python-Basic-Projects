from tkinter import *
from tkinter import messagebox

def newTask(event=None):
    task = my_entry.get()
    if task != "":
        lb.insert(END, (task, False))
        my_entry.delete(0, "end")
        update_gantt_chart()

def deleteTask():
    selected_task_index = lb.curselection()
    if selected_task_index:
        lb.delete(selected_task_index)
        update_gantt_chart()

def updateCompletionStatus():
    selected_task_index = lb.curselection()
    if selected_task_index:
        task, completion_status = lb.get(selected_task_index[0])
        lb.delete(selected_task_index)
        lb.insert(END, (f"✅ {task}", True))
        update_gantt_chart()

def update_gantt_chart(*args):
    canvas.delete("all")
    tasks = lb.get(0, END)

    bar_height = 30
    bar_spacing = 10
    text_spacing = 20  # Adjusted spacing for task names

    # Calculate canvas height based on the number of tasks
    canvas_height = max(len(tasks) * (bar_height + bar_spacing), 300)
    canvas.config(scrollregion=(0, 0, canvas.winfo_width(), canvas_height))

    for i, (task, completion_status) in enumerate(tasks):
        color = 'green' if completion_status else 'blue'
        bar_width = canvas.winfo_width() if completion_status else 0

        # Draw task name on the left
        canvas.create_text(text_spacing, i * (bar_height + bar_spacing) + bar_height / 2, text=task, anchor='w', font=('Arial', 12), fill='black')

        # Draw completion bar
        canvas.create_rectangle(text_spacing + len(task) * 8, i * (bar_height + bar_spacing), text_spacing + len(task) * 8 + bar_width, (i + 1) * (bar_height + bar_spacing), fill=color)

    # Update the scrollbar
    ysb.config(command=canvas.yview)

# GUI Setup
ws = Tk()
ws.geometry('500x600+500+200')
ws.title('To-Do List with Gantt Chart')
ws.config(bg='#FFB6C1')  # Set background color to light pink
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=30,
    height=10,
    font=('Arial', 16),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)

lb.pack(side=LEFT, fill=BOTH)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=Y)
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('Arial', 16)
)

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('Arial', 14),
    bg='#c5f776',  # Set button color to light purple
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('Arial', 14),
    bg='#ff8b61',  # Set button color to light purple
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

updateStatus_btn = Button(
    button_frame,
    text='Mark Completed',
    font=('Arial', 14),
    bg='#61c0ff',  # Set button color to light purple
    padx=20,
    pady=10,
    command=updateCompletionStatus
)
updateStatus_btn.pack(fill=BOTH, expand=True, side=LEFT)

gantt_frame = Frame(ws)
gantt_frame.pack(pady=10)

# Create a canvas with a vertical scrollbar
canvas = Canvas(gantt_frame, width=400, bg='white')
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Create a vertical scrollbar and associate it with the canvas
ysb = Scrollbar(gantt_frame, orient=VERTICAL, command=canvas.yview)
ysb.pack(side=RIGHT, fill=Y)
canvas.config(yscrollcommand=ysb.set)

# Bind the update_gantt_chart function to any changes in the canvas view
canvas.bind("<Configure>", update_gantt_chart)

update_gantt_chart()  # Initial update

# Bind the Enter key to the newTask function
ws.bind('<Return>', newTask)

ws.mainloop()
