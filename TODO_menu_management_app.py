# Update Menu from loaded json file

# Imports
import os
import sqlite3
from pathlib import Path
from modules.data_handling import load_menu

# Point to current directory
os.chdir(Path(__file__).parent)

# Path to DB
DB_FILE_PATH = 'db/acasa.db'

# Load menu from json file and save as dict
menu = load_menu('db/menu_2023.json')

# Connect to DB
db = sqlite3.connect(DB_FILE_PATH)
cursor = db.cursor()

# Delete tables (items + categories) testeb
with db:
    cursor.execute("DELETE FROM items;")
    cursor.execute("DELETE FROM categories;")

# Insert menu from dict into DB
# Create List of categories
categories = []
for id, category in enumerate(menu.keys(), start=1):
    categories.append((id, category))
    
# print(categories)    

sql_category = "INSERT INTO categories (category_id, title) VALUES (?, ?);"
sql_items = "INSERT INTO items (item_id, name, current_price, FK_category_id) VALUES (?, ?, ?, ?);"

for category in categories:
    # print(category, type(category))
    with db:
        # Insert category name and get Primary Key
        cursor.execute(sql_category, category)
        
        # Get list of items for each category
        items = []
        for item in menu[category[1]]:
            # Create tuple for each item
            new_item = (item['id'], item['name'], item['price'], cursor.lastrowid)
            items.append(new_item)
        
        # Insert items into items table
        cursor.executemany(sql_items, items)

