import sqlite3

def init_db():
    conn = sqlite3.connect("orders.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY, 
        user_id INTEGER, 
        product_id INTEGER
    )""")
    conn.commit()
    conn.close()

def add_order(user_id, product_id):
    conn = sqlite3.connect("orders.db")
    c = conn.cursor()
    c.execute("INSERT INTO orders (user_id, product_id) VALUES (?, ?)", (user_id, product_id))
    conn.commit()
    conn.close()

def get_all_orders():
    conn = sqlite3.connect("orders.db")
    c = conn.cursor()
    c.execute("SELECT * FROM orders")
    orders = [{"id": row[0], "user_id": row[1], "product_id": row[2]} for row in c.fetchall()]
    conn.close()
    return orders
