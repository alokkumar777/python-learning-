import tkinter as tk
from tkinter import ttk, messagebox
from database import *

# Connect to the database
connect_db()

# Create the main application
root = tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("800x600")

# Title
title_label = tk.Label(root, text="Personal Expense Tracker", font=("Arial", 20))
title_label.pack(pady=10)

# Input Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=20)

# Input Widgets
date_label = tk.Label(input_frame, text="Date (YYYY-MM-DD):")
date_label.grid(row=0, column=0, padx=5, pady=5)
date_entry = tk.Entry(input_frame)
date_entry.grid(row=0, column=1, padx=5, pady=5)

category_label = tk.Label(input_frame, text="Category:")
category_label.grid(row=0, column=2, padx=5, pady=5)
category_entry = ttk.Combobox(input_frame, values=["Food", "Transport", "Entertainment", "Other"])
category_entry.grid(row=0, column=3, padx=5, pady=5)

description_label = tk.Label(input_frame, text="Description:")
description_label.grid(row=1, column=0, padx=5, pady=5)
description_entry = tk.Entry(input_frame)
description_entry.grid(row=1, column=1, padx=5, pady=5)

amount_label = tk.Label(input_frame, text="Amount:")
amount_label.grid(row=1, column=2, padx=5, pady=5)
amount_entry = tk.Entry(input_frame)
amount_entry.grid(row=1, column=3, padx=5, pady=5)

# Buttons
def add_expense():
    date = date_entry.get()
    category = category_entry.get()
    description = description_entry.get()
    amount = amount_entry.get()
    
    if not date or not category or not description or not amount:
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    try:
        add_transaction(date, category, description, float(amount))
        refresh_table()
        messagebox.showinfo("Success", "Transaction added successfully!")
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a number.")

add_button = tk.Button(input_frame, text="Add Transaction", command=add_expense)
add_button.grid(row=2, column=1, pady=10)

# Transaction Table
table_frame = tk.Frame(root)
table_frame.pack(pady=20)

columns = ("ID", "Date", "Category", "Description", "Amount")
transaction_table = ttk.Treeview(table_frame, columns=columns, show="headings")
transaction_table.pack()

for col in columns:
    transaction_table.heading(col, text=col)
    transaction_table.column(col, width=100)

def refresh_table():
    for row in transaction_table.get_children():
        transaction_table.delete(row)
    for row in view_transactions():
        transaction_table.insert("", "end", values=row)

refresh_table()

# Delete Button
def delete_selected():
    selected_item = transaction_table.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "No transaction selected.")
        return

    transaction_id = transaction_table.item(selected_item, "values")[0]
    delete_transaction(transaction_id)
    refresh_table()
    messagebox.showinfo("Success", "Transaction deleted successfully!")

delete_button = tk.Button(root, text="Delete Selected", command=delete_selected)
delete_button.pack(pady=10)

# Run the main loop
root.mainloop()
