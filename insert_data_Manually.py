# Import required modules
from db import get_connection


# Function to calculate total amount for an order
def calculate_total_amount(order_id, cur):
    cur.execute("""
        SELECT p.price, oi.quantity
        FROM order_items oi
        JOIN products p ON oi.product_id = p.id
        WHERE oi.order_id = %s;
    """, (order_id,))
    items = cur.fetchall()
    total = sum(price * qty for price, qty in items)
    return total


# Function to insert customer manually
def insert_customer_manual():
    conn = get_connection()
    cur = conn.cursor()
    name = input("Enter customer name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    join_date = input("Enter join date (YYYY-MM-DD): ")

    cur.execute("""
        INSERT INTO customers (name, phone, email, join_date)
        VALUES (%s, %s, %s, %s);
    """, (name, phone, email, join_date))

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Customer inserted successfully.")


# Function to insert product manually
def insert_product_manual():
    conn = get_connection()
    cur = conn.cursor()
    name = input("Enter product name: ")
    description = input("Enter product description: ")
    price = float(input("Enter product price: "))

    cur.execute("""
        INSERT INTO products (name, description, price)
        VALUES (%s, %s, %s);
    """, (name, description, price))

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Product inserted successfully.")


# Function to insert order manually and return order_id
def insert_order_manual():
    conn = get_connection()
    cur = conn.cursor()
    customer_id = int(input("Enter customer ID (from the customers table): "))
    order_date = input("Enter order date (YYYY-MM-DD): ")

    cur.execute("""
        INSERT INTO orders (customer_id, order_date, total_amount)
        VALUES (%s, %s, %s)
        RETURNING id;
    """, (customer_id, order_date, total_amount))

    order_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ Order inserted with ID: {order_id}")
    return order_id


# Function to insert a single order item and update order amount
def insert_order_items_manual(order_id):
    conn = get_connection()
    cur = conn.cursor()

    # Ask for one product item and its quantity
    product_id = int(input("Enter product ID (from the products table): "))
    quantity = int(input("Enter quantity: "))

    # Fetch the product price from the products table
    cur.execute("""
        SELECT price FROM products WHERE id = %s;
    """, (product_id,))
    result = cur.fetchone()

    if result is None:
        print("❌ Invalid product ID.")
        cur.close()
        conn.close()
        return

    price = result[0]

    # Insert the product into order_items table with price
    cur.execute("""
        INSERT INTO order_items (order_id, product_id, quantity, price)
        VALUES (%s, %s, %s, %s);
    """, (order_id, product_id, quantity, price))

    # Recalculate and update total amount for the order
    total_amount = calculate_total_amount(order_id, cur)
    cur.execute("UPDATE orders SET total_amount = %s WHERE id = %s;", (total_amount, order_id))

    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ Order item added. Total Amount: ₹{total_amount:.2f}")

# Main function to call all manual data insertion functions
def main():
    print("🔧 Manual Data Insertion Script")

    while True:
        print("\nChoose the table you want to insert data into:")
        print("1. Insert Customer")
        print("2. Insert Product")
        print("3. Insert Order (with Items)")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == '1':
            insert_customer_manual()
        elif choice == '2':
            insert_product_manual()
        elif choice == '3':
            order_id = insert_order_manual()
            insert_order_items_manual(order_id)
        elif choice == '4':
            print("👋 Exiting the script.")
            break
        else:
            print("❌ Invalid choice, please choose a valid option.") #


if __name__ == "__main__":
    main()
##