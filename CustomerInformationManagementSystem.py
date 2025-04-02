import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Database setup
def setup_database():
    conn = sqlite3.connect("customers.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        birthday TEXT NOT NULL,
                        email TEXT NOT NULL,
                        phone TEXT NOT NULL,
                        address TEXT NOT NULL,
                        contact_method TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Function to submit customer data
def submit_data():
    name = entry_name.get()
    birthday = entry_birthday.get()
    email = entry_email.get()
    phone = entry_phone.get()
    address = entry_address.get()
    contact_method = contact_method_var.get()
    
    if not (name and birthday and email and phone and address and contact_method):
        messagebox.showerror("Error", "All fields are required!")
        return
    
    conn = sqlite3.connect("customers.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers (name, birthday, email, phone, address, contact_method) VALUES (?, ?, ?, ?, ?, ?)",
                   (name, birthday, email, phone, address, contact_method))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Success", "Customer information saved successfully!")
    clear_form()

# Function to clear form
def clear_form():
    entry_name.delete(0, tk.END)
    entry_birthday.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    contact_method_var.set("Select")

# Setup GUI
root = tk.Tk()
root.title("Customer Information Management System")
root.geometry("400x400")

# Labels and Entry Fields
tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Birthday (YYYY-MM-DD):").pack()
entry_birthday = tk.Entry(root)
entry_birthday.pack()

tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Phone:").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

tk.Label(root, text="Address:").pack()
entry_address = tk.Entry(root)
entry_address.pack()

# Dropdown for Contact Method
tk.Label(root, text="Preferred Contact Method:").pack()
contact_method_var = tk.StringVar()
contact_method_var.set("Select")
contact_method_menu = ttk.Combobox(root, textvariable=contact_method_var, values=["Email", "Phone", "Mail"])
contact_method_menu.pack()

# Submit Button
tk.Button(root, text="Submit", command=submit_data).pack()

setup_database()
root.mainloop()
