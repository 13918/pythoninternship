import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Calculator")
root.geometry("250x250")
root.resizable(False, False)
entry = tk.Entry(root, width=25, borderwidth=5, font=("Arial", 12))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
label = tk.Label(root, text="", font=("Arial", 12))
label.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
def calculate():
    try:
        # operation entry field
        result = eval(entry.get())
        # Display the result
        label.config(text="Result: " + str(result))
    except:
        messagebox.showerror("Error", "Invalid input")
def clear():
    entry.delete(0, tk.END)
    label.config(text="")
button_7 = tk.Button(root, text="7", padx=10, pady=5, command=lambda: entry.insert(tk.END, "7"))
button_8 = tk.Button(root, text="8", padx=10, pady=5, command=lambda: entry.insert(tk.END, "8"))
button_9 = tk.Button(root, text="9", padx=10, pady=5, command=lambda: entry.insert(tk.END, "9"))
button_divide = tk.Button(root, text="/", padx=12, pady=5, command=lambda: entry.insert(tk.END, "/"))
button_4 = tk.Button(root, text="4", padx=10, pady=5, command=lambda: entry.insert(tk.END, "4"))
button_5 = tk.Button(root, text="5", padx=10, pady=5, command=lambda: entry.insert(tk.END, "5"))
button_6 = tk.Button(root, text="6", padx=10, pady=5, command=lambda: entry.insert(tk.END, "6"))
button_multiply = tk.Button(root, text="*", padx=11, pady=5, command=lambda: entry.insert(tk.END, "*"))
button_1 = tk.Button(root, text="1", padx=10, pady=5, command=lambda: entry.insert(tk.END, "1"))
button_2 = tk.Button(root, text="2", padx=10, pady=5, command=lambda: entry.insert(tk.END, "2"))
button_3 = tk.Button(root, text="3", padx=10, pady=5, command=lambda: entry.insert(tk.END, "3"))
button_subtract = tk.Button(root, text="-", padx=12, pady=5, command=lambda: entry.insert(tk.END, "-"))
button_0 = tk.Button(root, text="0", padx=10, pady=5, command=lambda: entry.insert(tk.END, "0"))
button_decimal = tk.Button(root, text=".", padx=12, pady=5, command=lambda: entry.insert(tk.END, "."))
button_equal = tk.Button(root, text="=", padx=10, pady=5, command=calculate)
button_add = tk.Button(root, text="+", padx=11, pady=5, command=lambda: entry.insert(tk.END, "+"))
button_clear = tk.Button(root, text="Clear", padx=5, pady=5, command=clear)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_divide.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_subtract.grid(row=4, column=3)

button_0.grid(row=5, column=0)
button_decimal.grid(row=5, column=1)
button_equal.grid(row=5, column=2)
button_add.grid(row=5, column=3)

button_clear.grid(row=6, column=0, columnspan=4)
root.mainloop()