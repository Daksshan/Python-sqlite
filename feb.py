import sqlite3
def create_table():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 cell_number TEXT NOT NULL,
                 email TEXT)''')
    conn.commit()
    conn.close()
def insert_data(name, cell_number, email):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''INSERT INTO contacts (name, cell_number, email) VALUES (?, ?, ?)''',
              (name, cell_number, email))
    conn.commit()
    conn.close()
def fetch_all_data():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM contacts''')
    data = c.fetchall()
    conn.close()
    return data
create_table()
insert_data('John Doe', '123-456-7890', 'john@example.com')
insert_data('Jane Smith', '456-789-0123', 'jane@example.com')
insert_data('Alice Johnson', '789-012-3456', 'alice@example.com')
insert_data('Bob Williams', '234-567-8901', 'bob@example.com')
insert_data('Charlie Brown', '567-890-1234', 'charlie@example.com')
contacts = fetch_all_data()
print("Contacts:")
for contact in contacts:
    print(contact)
