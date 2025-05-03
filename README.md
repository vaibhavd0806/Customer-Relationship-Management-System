# Customer-Relationship-Management-System
---
## 📘 CRM PostgreSQL Data Insertion Project

This project is designed to simulate a CRM (Customer Relationship Management) system using PostgreSQL and Python. It provides two main ways to insert data into the database: **automated (using Faker)** and **manual (via user input)**.

---

### 📂 Project Structure

```
├── db.py                    # PostgreSQL connection module
├── insert_data_automated.py # Insert fake data using Faker
├── insert_data_manually.py  # Insert data manually via CLI
└── README.md                # You're here!
```

---

### 🔧 Requirements

Install the required Python modules using:

```bash
pip install psycopg2 faker
```

Ensure PostgreSQL is installed and running locally with a database named:

```bash
crm_system
```

---

### 🔗 Database Connection Configuration

File: `db.py`

```python
psycopg2.connect(
    host="localhost",
    database="crm_system",
    user="postgres",
    password="admin123"
)
```

Modify credentials as per your local PostgreSQL setup if needed.

---
## Database Schema

The CRM system uses the following tables:

### 📌 Features

#### ✅ 1. Automated Data Insertion (with Faker)

File: `insert_data_automated.py`

* Inserts:

  * 1000 customers
  * 6 fixed products
  * 500 orders
  * 1000 order items
* Use this to generate large test datasets quickly.

Run with:

```bash
python insert_data_automated.py
```

---

#### ✍️ 2. Manual Data Insertion (CLI Prompts)

File: `insert_data_manually.py`

* Insert individual:

  * Customers
  * Products
  * Orders and related items (with total amount calculation)

Run with:

```bash
python insert_data_manually.py
```

You will be prompted to select and enter data manually.

---

### 🗃️ Tables Overview

1. **customers**

   * `id`, `name`, `phone`, `email`, `join_date`

2. **products**

   * `id`, `name`, `description`, `price`

3. **orders**

   * `id`, `customer_id`, `order_date`, `total_amount`

4. **order\_items**

   * `id`, `order_id`, `product_id`, `quantity`, `price`

---

### 🧠 Key Concepts Used

* PostgreSQL with Python (`psycopg2`)
* Faker for synthetic data
* Manual CLI interaction using `input()`
* Foreign key relationships
* Order total calculation logic

---

### 📞 Contact

Built by **Vaibhav Dhotre**
📧 \vaibhavdhotre0806@gmail.com

🙋‍♂️ More About Me
🔗 [Connect with me on LinkedIn](https://www.linkedin.com/in/vaibhavd08/)

---
