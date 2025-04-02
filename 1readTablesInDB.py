import sqlite3

def read_all_customers():
    """Reads and prints all customer data from the database."""
    try:
        conn = sqlite3.connect('customer_data.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.close()
        return rows #returns the list of tuples
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None

def read_customer_by_name(name):
    """Reads and prints customer data based on the provided name."""
    try:
        conn = sqlite3.connect('customer_data.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE name = ?", (name,))
        rows = cursor.fetchall()
        for row in rows:
          print(row)
        conn.close()
        return rows #returns the list of tuples.
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Example usage:
    print("\n--- All Customers ---")
    read_all_customers()

    print("\n--- Customer by Name (Example) ---")
    read_customer_by_name("John Doe") #example.