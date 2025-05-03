# Import Required Modules
# Faker generates fake names, emails, phone numbers, etc.
# get_connection() is your custom function (from db.py) to connect to PostgreSQL.
# random is imported for future use (e.g., in generating purchases/interactions).

from faker import Faker
from db import get_connection
import random

# Creates a Faker object to call its data-generating methods like fake.name(), fake.email(), etc.
fake = Faker()

# Function to insert n number of customers (default is 1000).
def insert_customers(n=1000):
    # Establish a connection and get a cursor for executing SQL commands.
    conn = get_connection()
    cur = conn.cursor()
    print("Connected to database:", conn.get_dsn_parameters()["dbname"])

    # Generates:
    # name: Random person’s name
    # phone: Random phone number
    # email: Unique random email
    # join_date: A date within the last 3 years
    for _ in range(n):
        name = fake.name()
        phone = fake.phone_number()[:15]  # Ensures it doesn't exceed 15 characters
        email = fake.unique.email()
        join_date = fake.date_between(start_date='-3y', end_date='today')

        # Inserts each customer into the customers table using parameterized SQL (prevents SQL injection)
        cur.execute("""
            INSERT INTO customers (name, phone, email, join_date)
            VALUES (%s, %s, %s, %s);
        """, (name, phone, email, join_date))

    # Commits the transaction and closes everything properly.
    conn.commit()
    cur.close()
    conn.close()
    print(f"{n} customers inserted.")

# A hardcoded list of product entries

# ----------------------------
# FUNCTION TO INSERT PRODUCTS
# ----------------------------
def insert_products(n=6):
    # Hardcoded list of products (id will auto-generate)
    products = [
        ("Laptop", "High-performance laptop", 75000),
        ("Smartphone", "Latest model with great camera", 45000),
        ("Vacuum Cleaner", "Powerful vacuum cleaner for home", 12000),
        ("T-Shirt", "Comfortable cotton t-shirt", 800),
        ("Shoes", "Stylish and durable shoes", 2500),
        ("Blender", "Efficient kitchen blender", 1800)
    ]

    conn = get_connection()
    cur = conn.cursor()

    for name, description, price in products:
        cur.execute("""
            INSERT INTO products (name, description, price)
            VALUES (%s, %s, %s);
        """, (name, description, price))

    conn.commit()
    cur.close()
    conn.close()
    print("Products inserted.")

# Function to insert orders (you can specify the number of orders).
def insert_orders(n=100):
    # Generate random customer IDs and order details
    conn = get_connection()
    cur = conn.cursor()

    for _ in range(n):
        customer_id = random.randint(1, 1000)  # Assuming you have 1000 customers
        order_date = fake.date_this_year()
        total_amount = random.randint(1000, 50000)

        cur.execute("""
            INSERT INTO orders (customer_id, order_date, total_amount)
            VALUES (%s, %s, %s);
        """, (customer_id, order_date, total_amount))

    conn.commit()
    cur.close()
    conn.close()
    print(f"{n} orders inserted.")

# Function to insert order items (you can specify the number of order items).
def insert_order_items(n=200):
    conn = get_connection()
    cur = conn.cursor()

    for _ in range(n):
        order_id = random.randint(1, 100)  # Assuming you have 100 orders
        product_id = random.randint(1, 6)  # Assuming you have 6 products
        quantity = random.randint(1, 5)
        price = random.randint(1000, 50000)  # Random price range

        cur.execute("""
            INSERT INTO order_items (order_id, product_id, quantity, price)
            VALUES (%s, %s, %s, %s);
        """, (order_id, product_id, quantity, price))

    conn.commit()
    cur.close()
    conn.close()
    print(f"{n} order items inserted.")

if __name__ == "__main__":
    # Specify the exact number of records for each table
    insert_customers(1000)    # Insert 1000 customers
    insert_products(6)        # Insert 6 products (this is a fixed number in this case)
    insert_orders(500)        # Insert 500 orders
    insert_order_items(1000)  # Insert 1000 order items

#