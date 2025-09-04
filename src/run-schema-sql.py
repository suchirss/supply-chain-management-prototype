import sqlite3
import os 

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
db_dir_name = "db"

db_name = "supply_chain.db"
db_file = os.path.join(parent_dir, db_dir_name, db_name)

schema_name = "schema.sql"
schema_file = os.path.join(parent_dir, db_dir_name, schema_name)

with open(schema_file, "r", encoding="utf-8") as file:
    schema_sql = file.read()
    file.close()

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.executescript(schema_sql)
conn.commit()
conn.close()