#import os
import tkinter as tk
from tkinter import messagebox
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#e1e8ed")
        self.tasks = []
        self.setup_ui()

    def setup_ui(self):
        # Title
        tk.Label(self.root, text="To-Do List", font=("Arial", 20, "bold"),
                 bg="#e1e8ed", fg="#333").pack(pady=10)
        # Input Frame
        input_frame = tk.Frame(self.root, bg="#e1e8ed")
        input_frame.pack(pady=10)
        self.task_entry = tk.Entry(input_frame, font=("Arial", 12), width=30)
        self.task_entry.pack(side=tk.LEFT, padx=10)
        tk.Button(input_frame, text="Add Task", font=("Arial", 10, "bold"),
                  bg="#4caf50", fg="white", command=self.add_task).pack(side=tk.LEFT)
        # List Box
        list_frame = tk.Frame(self.root, bg="#e1e8ed")
        list_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        self.task_listbox = tk.Listbox(list_frame, font=("Arial", 12),
                                       width=45, height=10, activestyle="none")
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)
        # Status Label
        self.info_label = tk.Label(self.root, text="", font=("Arial", 11),
                                   bg="#e1e8ed", fg="blue")
        self.info_label.pack(pady=5)
        # Action Buttons
        button_frame = tk.Frame(self.root, bg="#e1e8ed")
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Mark as Done", font=("Arial", 11, "bold"),
                  bg="#2196f3", fg="white", command=self.mark_done).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Delete Task", font=("Arial", 11, "bold"),
                  bg="#f44336", fg="white", command=self.delete_task).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Clear All", font=("Arial", 11, "bold"),
                  bg="#757575", fg="white", command=self.clear_all).pack(side=tk.LEFT, padx=5)

    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks, 1):
            status = "✅" if task["done"] else "❌"
            self.task_listbox.insert(tk.END, f"{index}. {task['task']} [{status}]")

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append({"task": task_text, "done": False})
            self.task_entry.delete(0, tk.END)
            self.info_label.config(text=f"Task '{task_text}' added")
            self.refresh_listbox()
        else:
            self.info_label.config(text="Please enter a task first")

    def get_selected_index(self):
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a task first")
            return None
        return selection[0]

    def mark_done(self):
        index = self.get_selected_index()
        if index is not None:
            self.tasks[index]["done"] = True
            self.info_label.config(text="Task marked as done")
            self.refresh_listbox()

    def delete_task(self):
        index = self.get_selected_index()
        if index is not None:
            removed = self.tasks.pop(index)
            self.info_label.config(text=f"Deleted task: {removed['task']}")
            self.refresh_listbox()

    def clear_all(self):
        if not self.tasks:
            self.info_label.config(text="No tasks to clear")
            return
        if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
            self.tasks.clear()
            self.refresh_listbox()
            self.info_label.config(text="All tasks cleared")

if __name__ == '__main__':
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()


