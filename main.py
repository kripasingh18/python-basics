import customtkinter as ctk
from tkinter import messagebox

# Set appearance
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class TodoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("To-Do List")
        self.geometry("500x550")
        
        # UI Setup
        self.label = ctk.CTkLabel(self, text="My Tasks", font=("Arial", 24, "bold"))
        self.label.pack(pady=20)

        # Input Area
        self.entry_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.entry_frame.pack(pady=10, padx=20, fill="x")
        
        self.task_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Enter a new task...")
        self.task_entry.pack(side="left", expand=True, fill="x", padx=(0, 10))
        self.task_entry.bind('<Return>', lambda event: self.add_task())
        
        self.add_button = ctk.CTkButton(self.entry_frame, text="Add", width=70, command=self.add_task)
        self.add_button.pack(side="right")

        # Scrollable Task List
        self.task_frame = ctk.CTkScrollableFrame(self, label_text="Task List")
        self.task_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        self.tasks = []

        # Action Buttons
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=20)
        
        ctk.CTkButton(self.button_frame, text="Mark Done", command=self.mark_done).pack(side="left", padx=5)
        ctk.CTkButton(self.button_frame, text="Delete", fg_color="#f44336", hover_color="#d32f2f", command=self.delete_task).pack(side="left", padx=5)

    def add_task(self):
        text = self.task_entry.get().strip()
        if text:
            # Create a frame for each task row
            row = ctk.CTkFrame(self.task_frame)
            row.pack(fill="x", pady=2)
            
            check = ctk.CTkCheckBox(row, text=text, font=("Arial", 14))
            check.pack(side="left", padx=10, pady=5)
            
            self.tasks.append({"widget": row, "checkbox": check})
            self.task_entry.delete(0, "end")
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def mark_done(self):
        for item in self.tasks:
            if item["checkbox"].get() == 1:
                # Strike-through effect by changing font
                item["checkbox"].configure(font=("Arial", 14, "overstrike"), state="disabled")

    def delete_task(self):
        # Remove only the checked tasks
        for item in self.tasks[:]:
            if item["checkbox"].get() == 1:
                item["widget"].destroy()
                self.tasks.remove(item)

if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()