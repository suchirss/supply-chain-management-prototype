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

# function to Connect, Execute query, Close (CEC) cursor
def CEC_cursor(query_to_execute):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(query_to_execute)
    conn.commit()
    conn.close()

def create_order(client_name, product_name, SKU, quantity, status):
    insert_order_query = f"""
        INSERT INTO orders (client_name, order_name, SKU, quantity, status)
        VALUES ('{client_name}', '{product_name}', {SKU}, '{quantity}', '{status}')
    """
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(insert_order_query)
    conn.commit()
    conn.close()

create_order("TestClient", "TestProduct", "2999", 40, "TestStatus")    

def retrieve_order(table_name, *args):
    select_string = []

    if not args:
        select_string.append("*")
    else:
        for key in args:
            key = str(key) # ensure key is of string type
            select_string.append(f"{key}")

    select_string = ", ".join(select_string)

    retrieve_order_query = f"""
        SELECT {select_string} FROM {table_name}
    """

    
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(retrieve_order_query)
    retrieved_string = cursor.fetchall()
    conn.commit()   
    conn.close()

    return retrieved_string

def update_order(where_clause='', **kwargs):
    if not kwargs:
        print("No fields to update")
        return
    
    set_string = []
    for key, value in kwargs.items():
        set_string.append(f"{key} = '{value}'")

    set_string = ", ".join(set_string)

    update_order_query = f"""
        UPDATE orders
        SET {set_string}
        WHERE {where_clause}
    """

    # print(update_order_query)

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(update_order_query)
    conn.commit()
    conn.close()

update_order(where_clause="order_id = 2", client_name="test_client", order_name="test_name")

def delete_order(order_id):
    remove_order_query = f"""
        DELETE FROM orders WHERE order_id={order_id}
    """     
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(remove_order_query)
    conn.commit()
    conn.close()

# delete_order(4)

