import sqlite3


def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE store(item TEXT, quantity INTEGER, price INTEGER )")
    conn.commit()
    conn.close()


def insert_values(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()


insert_values('coffee cup', 8, 40)


def view_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    row=cur.fetchall()
    conn.close()
    return row


def delete_item(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item, ))
    conn.commit()
    conn.close()


def update_item(quantity, price, item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    conn.commit()
    conn.close()



update_item(30, 50,'coffee cup')

delete_item("water glass")

print(view_table())
