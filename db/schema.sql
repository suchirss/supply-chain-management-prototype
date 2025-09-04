PRAGMA foreign_keys = ON;

--- drop old tables if they exist ---
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS warehouse_inventory;

--- create orders table ---
CREATE TABLE orders (
        order_ID INTEGER PRIMARY KEY,
        client_name text NOT NULL,
        order_name text NOT NULL,
        SKU INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        status text NOT NULL  
    );

--- seed orders table ---
INSERT INTO orders (order_ID, client_name, order_name, SKU, quantity, status)
    VALUES
    (1, 'DrinksRUs', 'Barefoot Moscato 700mL', 1112, 20, 'Processing'),
    (2, 'LiquorMart', 'Bud Lite 150mL', 1093, 50, 'Shipped'),
    (3, 'BeerStop', 'Fireball 500mL', 9814, 35, 'Delivered');

--- create warehouse_inventory table ---
CREATE TABLE warehouse_inventory(
        SKU INTEGER PRIMARY KEY,
        product_name text NOT NULL,
        quantity INTEGER
    );

--- seed warehouse_inventory table ---
INSERT INTO warehouse_inventory (SKU, product_name, quantity)
    VALUES
    (9814, 'Fireball 500mL', 0),
    (1093, 'Bud Lite 150mL', 500),
    (1112, 'Barefoot Moscato 700mL', 2000),
    (1399, 'CA Blue 20oz', 5),
    (8939, 'BC Clear 1L', 100);