import sqlite3

file = "supply_chain.db"

try:
  conn = sqlite3.connect(file)
  print("CREATED DATABASE: supply_chain.db")

  cursor = conn.cursor()
  print("CURSOR: ", cursor)
  
  # drop both tables if they exists 
  cursor.execute("DROP TABLE IF EXISTS orders")
  cursor.execute("DROP TABLE IF EXISTS warehouse_inventory")

  # create order table
  orders_table_creation_query = """
    CREATE TABLE orders (
        order_ID INTEGER PRIMARY KEY,
        client_name text NOT NULL,
        order_name text NOT NULL,
        SKU INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        status text NOT NULL  
    )
    """
  
  cursor.execute(orders_table_creation_query)
  print("CREATED TABLE: orders")

  populate_orders_table_initial_query = """
    INSERT INTO orders (order_ID, client_name, order_name, SKU, quantity, status)
    VALUES
    (1, 'DrinksRUs', 'Barefoot Moscato 700mL', 1112, 20, 'Processing'),
    (2, 'LiquorMart', 'Bud Lite 150mL', 1093, 50, 'Shipped'),
    (3, 'BeerStop', 'Fireball 500mL', 9814, 35, 'Delivered')
    """
  
  cursor.execute(populate_orders_table_initial_query)
  print("POPULATED TABLE: orders")
  
  # create warehouse table
  warehouse_inventory_table_creation_query = """
    CREATE TABLE warehouse_inventory(
        SKU INTEGER PRIMARY KEY,
        product_name text NOT NULL,
        quantity INTEGER
    )
    """
  
  cursor.execute(warehouse_inventory_table_creation_query)
  print("CREATED TABLE: warehouse_inventory")
  
  populate_warehouse_inventory_table_initial_query = """
    INSERT INTO warehouse_inventory (SKU, product_name, quantity)
    VALUES
    (9814, 'Fireball 500mL', 0),
    (1093, 'Bud Lite 150mL', 500),
    (1112, 'Barefoot Moscato 700mL', 2000),
    (1399, 'CA Blue 20oz', 5),
    (8939, 'BC Clear 1L', 100)
    """
  
  cursor.execute(populate_warehouse_inventory_table_initial_query)
  print("POPULATED TABLE: warehouse_inventory")

  conn.commit()
  print("changes committed")
  
except sqlite3.Error as error:
  print("error occured: ", error)

