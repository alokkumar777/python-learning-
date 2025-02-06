import sqlite3

def connect_db():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY,
                        date TEXT,
                        category TEXT,
                        description TEXT,
                        amount REAL
                     )''')
    conn.commit()
    conn.close()

def add_transaction(date, category, description, amount):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (date, category, description, amount) VALUES (?, ?, ?, ?)", 
                   (date, category, description, amount))
    conn.commit()
    conn.close()

def view_transactions():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_transaction(transaction_id):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
    conn.commit()
    conn.close()
