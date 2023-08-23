5############################################################## TO DO LIST ##################################################################### 

import tkinter as tk
from tkinter import messagebox

########################### Create the main application window and define global variables ######################################################

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x700")
root.config(bg="#F97700")

tasks = []

################################################## Define functions for various actions ############################################################

#adding model

def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

######################################################## Deleting model ##############################################################################

def delete_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        del tasks[selected_index]
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")


########################################################## UPDATING MODEL ##############################################################################


def update_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        updated_task = entry_task.get()
        tasks[selected_index] = updated_task
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update!")

def update_listbox():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        listbox_tasks.insert(tk.END, task)

############################################################## Searching model ##########################################################################

def search_task():
    search_query = entry_search.get()
    if search_query:
        for index, task in enumerate(tasks):
            if search_query.lower() in task.lower():
                listbox_tasks.selection_clear(0, tk.END)
                listbox_tasks.select_set(index)
                listbox_tasks.activate(index)
                break
        else:
            messagebox.showinfo("Info", "Task not found!")
    else:
        messagebox.showwarning("Warning", "Please enter a search query!")


 ################################################################ CUSTOMIZATION ###########################################################################

label_title = tk.Label(root, text="Stylish To-Do List", font=("Helvetica", 30) , bg="#BFF8F6")
label_title.pack(pady=15)

entry_task = tk.Entry(root,font=("Helvetica", 14))
entry_task.pack(pady=10, padx=20)

btn_add_task = tk.Button(root, text="Add Task", command=add_task, font=("Helvetica", 12), bg="#FFD699")
btn_add_task.pack(pady=5)

listbox_tasks = tk.Listbox(root, font=("Helvetica", 12), selectbackground="#FFD699", selectforeground="black", bg="#F2F2F2")
listbox_tasks.pack(pady=20, padx=30, fill=tk.BOTH, expand=True)

btn_delete_task = tk.Button(root, text="Delete Task", command=delete_task, font=("Helvetica", 12), bg="#FF9999")
btn_delete_task.pack(pady=5)

btn_update_task = tk.Button(root, text="Update Task", command=update_task, font=("Helvetica", 12), bg="#99CCFF")
btn_update_task.pack(pady=5)

label_search = tk.Label(root, text="Search Task:", font=("Helvetica", 12), bg="#F2E5D8")
label_search.pack(pady=5)

############################################################## Entry for Search ############################################################################# 

entry_search = tk.Entry(root, font=("Helvetica", 12))
entry_search.pack(pady=5, padx=20)

btn_search_task = tk.Button(root, text="Search", command=search_task, font=("Helvetica", 12), bg="#B3FFCC")
btn_search_task.pack(pady=5)

root.mainloop()

