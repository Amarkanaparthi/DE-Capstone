import os
import random
import datetime as dt

import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv

load_dotenv()
random.seed(42)  # same data every run

FIRST = ["Aarav", "Diya", "Rohan", "Meera", "Kabir", "Isha", "Arjun", "Nisha", "Vihaan", "Anaya"]
LAST = ["Sharma", "Reddy", "Patel", "Nair", "Singh", "Rao", "Gupta", "Iyer", "Khan", "Das"]
CITIES = ["Hyderabad", "Bengaluru", "Mumbai", "Chennai", "Delhi", "Pune"]
CATEGORIES = ["Electronics", "Home", "Books", "Clothing", "Sports"]
STATUSES = ["completed", "shipped", "cancelled", "returned"]
WEIGHTS = [70, 15, 10, 5]

DDL = """
DROP TABLE IF EXISTS order_items, orders, products, customers CASCADE;
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    city TEXT,
    signup_date DATE NOT NULL
);
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price NUMERIC(10, 2) NOT NULL CHECK (price > 0)
);
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(customer_id),
    order_date DATE NOT NULL,
    status TEXT NOT NULL
);
CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL REFERENCES orders(order_id),
    product_id INTEGER NOT NULL REFERENCES products(product_id),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price NUMERIC(10, 2) NOT NULL
);
"""


def rand_date(start, end):
    return start + dt.timedelta(days=random.randint(0, (end - start).days))


def main():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"), user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )
    cur = conn.cursor()
    cur.execute(DDL)

    customers = []
    for i in range(1, 201):
        f, l = random.choice(FIRST), random.choice(LAST)
        customers.append((i, f"{f} {l}", f"{f.lower()}.{l.lower()}{i}@example.com",
                          random.choice(CITIES),
                          rand_date(dt.date(2024, 1, 1), dt.date(2025, 6, 30))))
    execute_values(cur, "INSERT INTO customers VALUES %s", customers)

    products, price_of = [], {}
    for i in range(1, 41):
        cat = random.choice(CATEGORIES)
        price = round(random.uniform(5, 500), 2)
        products.append((i, f"{cat} item {i}", cat, price))
        price_of[i] = price
    execute_values(cur, "INSERT INTO products VALUES %s", products)

    orders, items, item_id = [], [], 1
    for o in range(1, 1001):
        orders.append((o, random.randint(1, 200),
                       rand_date(dt.date(2025, 1, 1), dt.date(2026, 10, 31)),
                       random.choices(STATUSES, WEIGHTS)[0]))
        for p in random.sample(range(1, 41), random.randint(1, 4)):
            items.append((item_id, o, p, random.randint(1, 3), price_of[p]))
            item_id += 1
    execute_values(cur, "INSERT INTO orders VALUES %s", orders)
    execute_values(cur, "INSERT INTO order_items VALUES %s", items)

    conn.commit()
    for t in ("customers", "products", "orders", "order_items"):
        cur.execute(f"SELECT COUNT(*) FROM {t}")
        print(t, cur.fetchone()[0])
    conn.close()


if __name__ == "__main__":
    main()