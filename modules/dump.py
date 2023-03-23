from modules.classes import Category, Item, Customer, Order
import sqlite3
from pathlib import Path


# obsolete
def create_categories(menu:dict) -> list[object]:
    """To create category instances

    Args:
        menu (dict): Contains whole menu with categories and items

    Returns:
        list[object]: List of category instances
    """
    # Create empty list for category instances
    categories = []
    
    # Iterate over menu keys (category titles)
    for category_id, category_title in enumerate(menu, start=1):
        # Create category instances with id / title
        category = Category(category_id, category_title)
        categories.append(category)

    return categories

# obsolete
def create_items(menu:dict) -> list[object]:
    """To create item instances

    Args:
        menu (dict): Contains whole menu with categories and items

    Returns:
        list[object]: List of item instances
    """
    # Create empty list for item instances
    items = []
    
    # Iterate over all categories
    for category_id, category_title in enumerate(menu, start=1):
        # Iterate over all items within category
        for item in menu[category_title]:
            # Create item instance with id / name / price / category_id
            item = Item(item["id"], item["name"], item["price"], category_id)
            items.append(item)
            
    return items

def establish_db_connection(DB_FILE_PATH:Path) -> object:
    """Connects to SQLite DB

    Args:
        DB_FILE_PATH (Path): Path to DB file

    Returns:
        object: Returns DB connection and cursor
    """
    
    # Connect to DB
    db = sqlite3.connect(DB_FILE_PATH)
    # Create cursor for connection
    cursor = db.cursor()
    
    return db, cursor

def load_menu_to_dict(cursor:object) -> dict[list]:
    """To get the categories and related items from SQLite DB and save them as a dictionary.

    Args:
        cursor (object): Cursor for DB queries

    Returns:
        dict[list]: Contains menu categories and items
    """
    # Create empty dictionary
    menu = {}
    
    # Get amount of categories
    cursor.execute("SELECT count(*) FROM categories;")
    n_categories = cursor.fetchone()[0]

    # Iterate n_categories times
    for category_id in range(1, n_categories + 1):
        # Get title from category depending on category_id
        cursor.execute(f"SELECT title FROM categories WHERE category_id = {category_id}")
        category_title = cursor.fetchone()[0]
        
        # Create empty list for menu["category"] e.g. menu["Pizzen"]
        menu[category_title] = []
        
        # Get all items (id, name, price) depending on category_id
        cursor.execute(f"SELECT item_id, name, current_price FROM items WHERE item_id LIKE '{category_id}%' ")
        # Create dictionary for each item
        for item in cursor:
            new_item = {"id" : int(item[0]),
                        "name" : str(item[1]),
                        "price" : float(item[2])}
            # Append dictionary to menu["category"]
            menu[category_title].append(new_item)
         
    return menu

def verify_customer(customer:object, cursor:object, db:object) -> int:
    # Get all customer_ids where first name and last name match with input
    cursor.execute(f"SELECT customer_id FROM customers WHERE first_name = '{customer.first_name}' AND last_name = '{customer.last_name}';") 
    # Save all found ids in list of tuples
    customer_ids = cursor.fetchall()
    
    # Check if customer_ids list is not empty
    if customer_ids:
        # Use first entry as id
        customer.id = customer_ids[0][0]
        print("\nKundendaten gefunden.")
    else:
        # Create a new entry in DB
        customer.id = customer.add_to_db(cursor, db)
        print("\nNeuer Kunde registriert.")
        
    print(f"Guten Tag {customer.first_name} {customer.last_name}. \nIhre KundenID lautet: {customer.id} \n")
    
    return customer