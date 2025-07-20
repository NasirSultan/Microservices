import sqlite3

def init_db():
    conn = sqlite3.connect("products.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, title TEXT)")
    conn.commit()
    conn.close()

def add_product(title):
    conn = sqlite3.connect("products.db")
    c = conn.cursor()
    c.execute("INSERT INTO products (title) VALUES (?)", (title,))
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect("products.db")
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = [{"id": row[0], "title": row[1]} for row in c.fetchall()]
    conn.close()
    return products
