import sqlite3

def read_all_customers():
    """Reads and prints all customer data from the database."""
    try:
        conn = sqlite3.connect('customer_data.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers")
        rows = cursor.fetchall()

        if not rows:
            print("No customers found in the database.")
            return []

        print("--- All Customers ---")
        for row in rows:
            print(f"Name: {row[0]}, Birthday: {row[1]}, Email: {row[2]}, Phone: {row[3]}, Address: {row[4]}, Contact: {row[5]}")

        conn.close()
        return rows  # Returns the list of tuples.
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

        if not rows:
            print(f"No customer found with the name '{name}'.")
            return []

        print(f"--- Customer '{name}' ---")
        for row in rows:
            print(f"Name: {row[0]}, Birthday: {row[1]}, Email: {row[2]}, Phone: {row[3]}, Address: {row[4]}, Contact: {row[5]}")

        conn.close()
        return rows  # Returns the list of tuples.
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Example usage:
    read_all_customers()

    print("\n--- Customer by Name (Example) ---")
    read_customer_by_name("John Doe")  # Example.