import tkinter as tk
from tkinter import messagebox
import sqlite3

class ContactList:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact List")
        self.conn = sqlite3.connect("contacts.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, name TEXT, number TEXT, email TEXT, address TEXT)")
        self.conn.commit()

        self.frame1 = tk.Frame(self.root)
        self.frame1.pack(fill="x")
        self.frame2 = tk.Frame(self.root)
        self.frame2.pack(fill="x")
        self.frame3 = tk.Frame(self.root)
        self.frame3.pack(fill="x")

        tk.Label(self.frame1, text="Name:").pack(side="left")
        self.name_entry = tk.Entry(self.frame1)
        self.name_entry.pack(side="left")
        tk.Label(self.frame1, text="Number:").pack(side="left")
        self.number_entry = tk.Entry(self.frame1)
        self.number_entry.pack(side="left")

        tk.Label(self.frame2, text="Email:").pack(side="left")
        self.email_entry = tk.Entry(self.frame2)
        self.email_entry.pack(side="left")
        tk.Label(self.frame2, text="Address:").pack(side="left")
        self.address_entry = tk.Entry(self.frame2)
        self.address_entry.pack(side="left")

        tk.Button(self.frame3, text="Add Contact", command=self.add_contact).pack(side="left")
        tk.Button(self.frame3, text="Delete Contact", command=self.delete_contact).pack(side="left")
        tk.Button(self.frame3, text="View Contacts", command=self.view_contacts).pack(side="left")
        tk.Button(self.frame3, text="Update Contact", command=self.update_contact).pack(side="left")

        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(fill="both", expand=True)


        self.load_contacts()

    def add_contact(self):
        name = self.name_entry.get()
        number = self.number_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name and number:
            self.cursor.execute("INSERT INTO contacts (name, number, email, address) VALUES (?, ?, ?, ?)", (name, number, email, address))
            self.conn.commit()
            self.listbox.insert("end", name)
            self.name_entry.delete(0, "end")
            self.number_entry.delete(0, "end")
            self.email_entry.delete(0, "end")
            self.address_entry.delete(0, "end")
        else:
            messagebox.showerror("Error", "Name and Number are required")

    def delete_contact(self):
        selected = self.listbox.curselection()
        if selected:
            name = self.listbox.get(selected)
            self.cursor.execute("DELETE FROM contacts WHERE name=?", (name,))
            self.conn.commit()
            self.listbox.delete(selected)

    def view_contacts(self):
        selected = self.listbox.curselection()
        if selected:
            name = self.listbox.get(selected)
            self.cursor.execute("SELECT * FROM contacts WHERE name=?", (name,))
            contact = self.cursor.fetchone()
            messagebox.showinfo("Contact Info", f"Name: {contact[1]}\nNumber: {contact[2]}\nEmail: {contact[3]}\nAddress: {contact[4]}")

    def update_contact(self):
        selected = self.listbox.curselection()
        if selected:
            name = self.listbox.get(selected)
            self.cursor.execute("SELECT * FROM contacts WHERE name=?", (name,))
            contact = self.cursor.fetchone()
            contact[1] = self.name_entry.get()
            contact[2] = self.number_entry.get()
            contact[3] = self.email_entry.get()
            contact[4] = self.address_entry.get()
            self.cursor.execute("UPDATE contacts SET name=?, number=?, email=?, address=? WHERE name=?", (contact[1], contact[2], contact[3], contact[4], name))
            self.conn.commit()
            self.name_entry.delete(0, "end")
            self.number_entry.delete(0, "end")
            self.email_entry.delete(0, "end")
            self.address_entry.delete(0, "end")

    def load_contacts(self):
        self.cursor.execute("SELECT name FROM contacts")
        contacts = self.cursor.fetchall()
        for contact in contacts:
            self.listbox.insert("end", contact[0])

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactList(root)
    root.mainloop()