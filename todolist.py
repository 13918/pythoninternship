import tkinter as tk

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.configure(background="#F7DC6F")  # yellow base box

        # Heading
        self.heading_label = tk.Label(root, text="To-Do List", font=("Arial", 24, "bold"), fg="#F2C464", bg="#FFA07A", relief="raised", bd=5)
        self.heading_label.pack(pady=10)

        # Text box area
        self.text_box = tk.Text(root, width=40, height=10, bg="#FFFFFF", fg="black", relief="sunken", bd=5)
        self.text_box.pack(pady=10)

        # Buttons
        self.button_frame = tk.Frame(root, bg="#F7DC6F")
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Text", command=self.add_text, fg="black", bg="#FFFFFF", relief="raised", bd=2)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Text", command=self.delete_text, fg="black", bg="#FFFFFF", relief="raised", bd=2)
        self.delete_button.pack(side=tk.LEFT, padx=5)

    def add_text(self):
        text = self.text_box.get("1.0", "end-1c")
        self.text_box.insert("end", "\n" + text)

    def delete_text(self):
        self.text_box.delete("1.0", "end")

root = tk.Tk()
todo_list = ToDoList(root)
root.mainloop()