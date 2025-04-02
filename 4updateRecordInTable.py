import sqlite3

def update_order_quantity(order_id, new_quantity):
    """Updates the quantity of an order in the 'orders' table."""
    try:
        conn = sqlite3.connect('customer_data.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE orders SET quantity = ? WHERE order_id = ?", (new_quantity, order_id))
        conn.commit()
        conn.close()
        print(f"Order {order_id} quantity updated to {new_quantity}.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def update_product_price(product_name, new_price):
    """Updates the price of a product in the 'products' table."""
    try:
        conn = sqlite3.connect('customer_data.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE products SET price = ? WHERE product_name = ?", (new_price, product_name))
        conn.commit()
        conn.close()
        print(f"Price for {product_name} updated to {new_price}.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def update_customer_order_date(customer_name, new_date):
    """Updates the order date for all orders from that customer."""
    try:
      conn = sqlite3.connect('customer_data.db')
      cursor = conn.cursor()
      cursor.execute("UPDATE orders SET order_date = ? WHERE customer_name = ?", (new_date, customer_name))
      conn.commit()
      conn.close()
      print(f"Order date for {customer_name} updated to {new_date}.")
    except sqlite3.Error as e:
      print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage:
    update_order_quantity(1, 10)  # Update order with ID 1 to quantity 10.
    update_product_price("Widget", 25.99)  # Update the price of "Widget" to 25.99.
    update_customer_order_date("John Doe", "2024-12-25") #update all John Doe order dates.