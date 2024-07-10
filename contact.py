import tkinter as tk
from tkinter import messagebox

class ContactList:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact List")
        self.contacts = {}

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
        tk.Button(self.frame3, text="Save Contacts", command=self.save_contacts).pack(side="left")

        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(fill="both", expand=True)

    def add_contact(self):
        name = self.name_entry.get()
        number = self.number_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name and number:
            self.contacts[name] = {"number": number, "email": email, "address": address}
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
            del self.contacts[name]
            self.listbox.delete(selected)

    def view_contacts(self):
        selected = self.listbox.curselection()
        if selected:
            name = self.listbox.get(selected)
            contact = self.contacts[name]
            messagebox.showinfo("Contact Info", f"Name: {name}\nNumber: {contact['number']}\nEmail: {contact['email']}\nAddress: {contact['address']}")

    def update_contact(self):
        selected = self.listbox.curselection()
        if selected:
            name = self.listbox.get(selected)
            contact = self.contacts[name]
            contact["number"] = self.number_entry.get()
            contact["email"] = self.email_entry.get()
            contact["address"] = self.address_entry.get()
            self.name_entry.delete(0, "end")
            self.number_entry.delete(0, "end")
            self.email_entry.delete(0, "end")
            self.address_entry.delete(0, "end")

    def save_contacts(self):
        with open("contacts.txt", "w") as f:
            for name, contact in self.contacts.items():
                f.write(f"{name}:{contact['number']}:{contact['email']}:{contact['address']}\n")
        messagebox.showinfo("Success", "Contacts saved successfully")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactList(root)
    root.mainloop()