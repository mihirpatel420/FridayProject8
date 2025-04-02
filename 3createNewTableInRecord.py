import sqlite3

def create_orders_table():
    """Creates a new 'orders' table in the customer_data.db database."""
    try:
        conn = sqlite3.connect('customer_data.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT,
                order_date TEXT,
                product TEXT,
                quantity INTEGER,
                price REAL,
                FOREIGN KEY (customer_name) REFERENCES customers(name)
            )
        ''')

        conn.commit()
        conn.close()
        print("Orders table created or already exists.")

    except sqlite3.Error as e:
        print(f"An error occurred while creating the orders table: {e}")

def create_products_table():
    """Creates a new 'products' table in the customer_data.db database."""
    try:
        conn = sqlite3.connect('customer_data.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT UNIQUE,
                description TEXT,
                price REAL
            )
        ''')

        conn.commit()
        conn.close()
        print("Products table created or already exists.")

    except sqlite3.Error as e:
        print(f"An error occurred while creating the products table: {e}")

if __name__ == "__main__":
    create_orders_table()
    create_products_table()