import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

def create_tables():
    cursor.execute('''CREATE TABLE IF NOT EXISTS Seller
                (id INTEGER PRIMARY KEY, name TEXT, types TEXT, quantity INTEGER, date TEXT, cost INTEGER)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Stock
                (id INTEGER PRIMARY KEY, name TEXT, quantity TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Buyer
                (id INTEGER PRIMARY KEY, name TEXT, phone INTEGER, types TEXT, quantity INTEGER,date TEXT, cost INTEGER)''')
    conn.commit()
    
# Insert data into table1
def insert_into_Seller(name, types, quantity, date, cost):
    cursor.execute("INSERT INTO Seller (name, types, quantity, date, cost) VALUES (?, ?, ?, ?, ?)", (name, types, quantity, date, cost))
    conn.commit()
    
# Insert data into table2
def insert_into_Stocks(name, quantity):
    cursor.execute("INSERT INTO Stocks (name, quantity) VALUES (?, ?)", (name, quantity))
    conn.commit()

# Insert data into table3
def insert_into_Buyer(name, phone, types, quantity, date, cost):
    cursor.execute("INSERT INTO table3 (name, phone, types, quantity, date, cost) VALUES (?, ?, ?, ?, ?, ?)", (name, phone, types, quantity, date, cost))
    conn.commit()

# Function to display data from a table
def display_table(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    data = cursor.fetchall()
    print(f"Data from {table_name}:")
    for row in data:
        print(row)

# Function to retrieve data from a table
def retrieve_data(table_name, column, value):
    cursor.execute(f"SELECT * FROM {table_name} WHERE {column}=?", (value,))
    data = cursor.fetchall()
    print(f"Retrieved data from {table_name}:")
    for row in data:
        print(row)

def update_Stocks(name, quantity):
    cursor.execute("UPDATE Stocks SET quantity=? WHERE name=?", (quantity, name))
    conn.commit()
    print("Data in table2 updated.")
    
# Example usage of functions
def main():
    create_tables()
    while True:
        table_name = input("Enter table name to insert information into :")
        if table_name == 'Seller':
            name = input("Enter name:")
            types = input("Enter type of product:")
            quantity = input("Enter quantity:")
            date = input ("Enter date:") 
            cost = input("Enter cost:")
            insert_into_Seller(name, types, quantity, date, cost)
        elif table_name == 'Stocks':
            name = input("Enter name:")
            quantity = input("Enter quantity:")
            insert_into_Stocks(name, quantity)
        elif table_name =='Buyer':
            name = input("Enter name:")
            phone = input("Enter phone number:")
            types = input("Enter type of product:")
            quantity = input("Enter quantity:")
            date = input("Enter date:")
            cost = input("Enter cost:")
            insert_into_Buyer(name, phone, types, quantity, date, cost)
        else:
            break

    update_Stocks('Los Angeles', 50)
    display_table("Stocks")
    
    table_name = input("Enter table name to be displayed:")
    display_table(table_name)

    table_name = input("Enter table name to retrieve data from:")
    column_name = input("Enter column name to retrieve data from:")
    value = input("Enter value of the column to match:")
    retrieve_data(table_name, column_name, value)
    
# Run the main function
if __name__ == "__main__":
    main()

# Close connection
conn.close()
