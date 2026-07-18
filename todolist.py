import tkinter as tk
from tkinter import messagebox

FILE_NAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            for task in file.readlines():
                task_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

def save_tasks():
    with open(FILE_NAME, "w") as file:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = task_entry.get().strip()
    if task == "":
        messagebox.showwarning("Warning", "Please enter a task.")
        return
    task_listbox.insert(tk.END, "☐ " + task)
    task_entry.delete(0, tk.END)
    save_tasks()

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")

def mark_completed():
    try:
        selected = task_listbox.curselection()[0]
        task = task_listbox.get(selected)
        if task.startswith("☐"):
            task = task.replace("☐", "✔", 1)
            task_listbox.delete(selected)
            task_listbox.insert(selected, task)
            save_tasks()
        else:
            messagebox.showinfo("Info", "Task is already completed.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")

def clear_tasks():
    if messagebox.askyesno("Confirm", "Delete all tasks?"):
        task_listbox.delete(0, tk.END)
        save_tasks()

root = tk.Tk()
root.title("To-Do List Application")
root.geometry("500x500")
root.resizable(False, False)
root.configure(bg="#f0f4f7")

title = tk.Label(root, text="📝 TO-DO LIST", font=("Arial", 20, "bold"), bg="#4CAF50", fg="white", pady=10)
title.pack(fill="x")

frame = tk.Frame(root, bg="#f0f4f7")
frame.pack(pady=15)

task_entry = tk.Entry(frame, width=35, font=("Arial", 12))
task_entry.grid(row=0, column=0, padx=5)

add_btn = tk.Button(frame, text="Add Task", width=12, bg="#4CAF50", fg="white", command=add_task)
add_btn.grid(row=0, column=1)

task_listbox = tk.Listbox(root, width=55, height=15, font=("Arial", 12), selectbackground="#2196F3")
task_listbox.pack(pady=10)

button_frame = tk.Frame(root, bg="#f0f4f7")
button_frame.pack()

complete_btn = tk.Button(button_frame, text="Mark Completed", width=15, bg="#2196F3", fg="white", command=mark_completed)
complete_btn.grid(row=0, column=0, padx=5, pady=5)

delete_btn = tk.Button(button_frame, text="Delete Task", width=15, bg="#f44336", fg="white", command=delete_task)
delete_btn.grid(row=0, column=1, padx=5, pady=5)

clear_btn = tk.Button(button_frame, text="Clear All", width=15, bg="#FF9800", fg="white", command=clear_tasks)
clear_btn.grid(row=0, column=2, padx=5, pady=5)

load_tasks()

root.mainloop()
