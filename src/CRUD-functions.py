# Create, Read, Update, Delete (CRUD) Functions
import sqlite3
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
db_dir_name = "db"
db_name = "supply_chain.db"
db_file = os.path.join(parent_dir, db_dir_name, db_name)
print(db_file)



# Orders Table CRUD 
def create_order(order_id, client_name, product_name, SKU, quantity, status):
    insert_order_query = f"""
        INSERT INTO orders(order_id, client_name, product_name, SKU, quantity, status)
        VALUES ({order_id}, {client_name}, {product_name}, {SKU}, {quantity}, {status})
    """
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(create_order)
    conn.commit()
    conn.close()

def remove_order(order_id):
    remove_order_query = f"""
        DELETE FROM orders WHERE order_id=${order_id}
    """     

def update_order(order_id, **kwargs):
    if not kwargs:
        print("No fields to update")
        return

update_order(4, check="check", one=1)