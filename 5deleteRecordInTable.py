import sqlite3

def delete_order(order_id):
    """Deletes an order from the 'orders' table based on the order_id."""
    try:
        conn = sqlite3.connect('customer_data.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM orders WHERE order_id = ?", (order_id,))
        conn.commit()
        conn.close()
        print(f"Order {order_id} deleted.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def delete_product(product_name):
    """Deletes a product from the 'products' table based on the product_name."""
    try:
        conn = sqlite3.connect('customer_data.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE product_name = ?", (product_name,))
        conn.commit()
        conn.close()
        print(f"Product '{product_name}' deleted.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def delete_customer_orders(customer_name):
  """Deletes all orders associated with a given customer name."""
  try:
    conn = sqlite3.connect('customer_data.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM orders WHERE customer_name = ?", (customer_name,))
    conn.commit()
    conn.close()
    print(f"All orders for customer '{customer_name}' deleted.")
  except sqlite3.Error as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage:
    delete_order(1)  # Delete order with ID 1.
    delete_product("Widget")  # Delete the product named "Widget".
    delete_customer_orders("Jane Smith") #Delete all orders from Jane Smith.