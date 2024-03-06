from tkinter import *
from tkinter import messagebox

tasks_list = []
counter = 1

def input_error():
    if enterTaskField.get() == "":
        messagebox.showerror("Input Error", "Task field cannot be empty")
        return False
    return True

def clear_task_number_field():
    taskNumberField.delete(0.0, END)

def clear_task_field():
    enterTaskField.delete(0, END)

def insert_task():
    global counter

    if not input_error():
        return

    content = enterTaskField.get() + "\n"
    tasks_list.append(content)

    TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)
    counter += 1

    clear_task_field()

def delete_task():
    global counter

    if len(tasks_list) == 0:
        messagebox.showerror("No task", "No tasks to delete")
        return

    number = taskNumberField.get(1.0, END)

    if number == "\n":
        messagebox.showerror("Input Error", "Task number cannot be empty")
        return
    else:
        task_no = int(number)

    clear_task_number_field()

    tasks_list.pop(task_no - 1)
    counter -= 1

    TextArea.delete(1.0, END)

    for i in range(len(tasks_list)):
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="cornsilk4")
    gui.title("ToDo App")
    gui.geometry("700x1000")

    enterTask = Label(gui, text="Enter Your Task", bg="cornsilk4", font=("Arial", 25))
    enterTaskField = Entry(gui, font=("Arial", 25))
    Submit = Button(gui, text="Submit", fg="black", bg="cornsilk3", font=("Arial", 25), command=insert_task)
    TextArea = Text(gui, height=10, width=35, font="lucida 25", bg="cornsilk3")
    taskNumber = Label(gui, text="Delete Task Number", bg="cornsilk3", font=("Arial", 25))
    taskNumberField = Text(gui, height=1, width=5, font=("Arial", 25))
    delete = Button(gui, text="Delete", fg="black", bg="cornsilk3", font=("Arial", 25), command=delete_task)

    enterTask.grid(row=0, column=2)
    enterTaskField.grid(row=1, column=2, ipadx=100)
    Submit.grid(row=2, column=2)
    TextArea.grid(row=3, column=2, padx=20, pady=10, sticky=W)
    taskNumber.grid(row=4, column=2, pady=10)
    taskNumberField.grid(row=5, column=2)
    delete.grid(row=6, column=2, pady=10)

    gui.mainloop()
