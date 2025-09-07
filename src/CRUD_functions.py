# Create, Read, Update, Delete (CRUD) Functions
import sqlite3
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
db_dir_name = "db"
db_name = "supply_chain.db"
db_file = os.path.join(parent_dir, db_dir_name, db_name)
# print(db_file)

# Orders Table CRUD 

# function to Connect, Execute query, Close (CEC) cursor
def CEC_cursor(query_to_execute, retrieve=False):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(query_to_execute)
    if retrieve == True:
        returned_string = cursor.fetchall()
    conn.commit()
    conn.close()

    if retrieve == True:
        return returned_string


def create_order(client_name, product_name, SKU, quantity, status):
    insert_order_query = f"""
        INSERT INTO orders (client_name, order_name, SKU, quantity, status)
        VALUES ('{client_name}', '{product_name}', {SKU}, '{quantity}', '{status}')
    """

    CEC_cursor(insert_order_query)

# create_order("TestClient", "TestProduct", "2999", 40, "TestStatus")    

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

    retrieved_string = CEC_cursor(retrieve_order_query, retrieve=True)

    return retrieved_string

print(retrieve_order("orders", "order_name"))

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

    CEC_cursor(update_order_query)

# update_order(where_clause="order_id = 4", client_name="xyz", order_name="xyz")

def delete_order(order_id):
    remove_order_query = f"""
        DELETE FROM orders WHERE order_id={order_id}
    """     
    CEC_cursor(remove_order_query)

# delete_order(8)

