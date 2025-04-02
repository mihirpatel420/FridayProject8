import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import re

def create_database():
    """Creates the database and table if they don't exist."""
    conn = sqlite3.connect('customer_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            name TEXT,
            birthday TEXT,
            email TEXT,
            phone TEXT,
            address TEXT,
            contact_method TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_customer(name, birthday, email, phone, address, contact_method):
    """Inserts customer data into the database."""
    conn = sqlite3.connect('customer_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO customers (name, birthday, email, phone, address, contact_method)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, birthday, email, phone, address, contact_method))
    conn.commit()
    conn.close()

def validate_email(email):
    """Validates email format."""
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_regex, email)

def validate_date(date_text):
    """Validates date format (YYYY-MM-DD)."""
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def submit_data():
    """Handles the submission of customer data."""
    name = name_entry.get()
    birthday = birthday_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    contact_method = contact_var.get()

    if not name or not birthday or not email or not phone or not address or not contact_method:
      messagebox.showerror("Error", "All fields are required.")
      return

    if not validate_email(email):
      messagebox.showerror("Error", "Invalid email format.")
      return

    if not validate_date(birthday):
      messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")
      return

    insert_customer(name, birthday, email, phone, address, contact_method)
    messagebox.showinfo("Success", "Customer data submitted successfully.")

    # Clear the form
    name_entry.delete(0, tk.END)
    birthday_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    contact_var.set("Email") #reset dropdown

# Create the main window
root = tk.Tk()
root.title("Customer Information System")

# Create labels and entry fields
tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Birthday (YYYY-MM-DD):").grid(row=1, column=0)
birthday_entry = tk.Entry(root)
birthday_entry.grid(row=1, column=1)

tk.Label(root, text="Email:").grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

tk.Label(root, text="Phone:").grid(row=3, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=3, column=1)

tk.Label(root, text="Address:").grid(row=4, column=0)
address_entry = tk.Entry(root)
address_entry.grid(row=4, column=1)

tk.Label(root, text="Preferred Contact Method:").grid(row=5, column=0)
contact_var = tk.StringVar(root)
contact_var.set("Email")  # Default value
contact_dropdown = ttk.Combobox(root, textvariable=contact_var, values=["Email", "Phone", "Mail"])
contact_dropdown.grid(row=5, column=1)

# Create the submit button
submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=6, column=0, columnspan=2, pady=10)

# Create the database
create_database()

# Start the GUI event loop
root.mainloop()