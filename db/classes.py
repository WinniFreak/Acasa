from db.db_manager import DBManager


class Category:
    """Template of a category
    """
    def __init__(self, id:int, title:str) -> None:
        """Build a categeory instance

        Args:
            id (int): Unique category id
            title (str): Category title
        """
        self.id = id
        self.title = title
        self.item_list = [] # Empty list for item instances
        self.db = DBManager()
        
    def __repr__(self) -> str:
        """To print necessary category information

        Returns:
            str: Returns title of category
        """
        return f"{self.title}"
    
    @staticmethod
    def get_categories() -> list[object]:
        """Returns a list of all categories in DB

        Returns:
            list[object]: Returns a list of category instances
        """
        
        # SQL command for selection of all categories
        sql_get_categories = "SELECT * FROM categories"
        
        # Execute SQL command via DBManager
        entries = DBManager().get_records(sql_get_categories)
        
        # Create a list of category instances
        categories = []
        
        for entry in entries:
            category = Category(entry[0], entry[1]) # id, title
            categories.append(category)
            
        return categories
    
    def add_category_to_db():
        """Adds the category to SQLite DB
        """
        # TODO
        pass

class Customer:
    """Template of a customer
    """
    def  __init__(self, id_:int, first_name:str, last_name:str) -> None:
        """Build a customer instance

        Args:
            id_ (int): Unique customer id
            first_name (str): First name of customer
            last_name (str): Last name of customer
        """
        self.id = id_ # id_ because id is a reserved function name
        self.first_name = first_name
        self.last_name = last_name
        self.db = DBManager()
        
        
    def __repr__(self) -> str:
        """To print necessary customer information

        Returns:
            str: Returns id / first name / last name of customer
        """
        return f"{self.id}. {self.first_name} {self.last_name}"
    
    def add_to_db(self) -> None:
        """Creates a new DB entry for customer instance and saves customer ID in self.id
        """
        # Save customer name in tuple
        data = (self.first_name, self.last_name)
        
        # SQL command for insertion of new customer
        sql_insert_customer = "INSERT INTO customers (first_name, last_name) VALUES (?, ?);"
       
        # Execute SQL command via DBManager and save customer ID in self.id
        self.id = self.db.insert_record(sql_insert_customer, data)
        
    @staticmethod
    def get_customer(first_name:str, last_name:str) -> object:
        """Check if customer already exists in DB and returns customer instance if it does

        Args:
            first_name (str): Customer first name
            last_name (str): Customer last name

        Returns:
            object: Customer instance
        """
        
        # Create tuple with customer name
        data = (first_name, last_name)
        
        # SQL command for selection of customer
        sql_select_customer = "SELECT * FROM customers WHERE first_name LIKE ? AND last_name LIKE ?;"
        
        # Get first entry from DB via DBManager
        entry = DBManager().get_record(sql_select_customer, data)
        
        # Create customer instance with data from DB if entry exists
        if entry:
            customer = Customer(entry[0], entry[1], entry[2]) # id, first_name, last_name
            return customer
        
    @classmethod
    def get_or_create_customer(cls, first_name:str, last_name:str) -> object:
        """Check if customer already exists in DB and returns customer instance if it does. If customer does not exist, a new customer instance is created and added to DB.

        Args:
            first_name (str): Customer first name
            last_name (str): Customer last name

        Returns:
            object: Customer instance
        """
        
        # Check if customer already exists in DB
        customer = Customer.get_customer(first_name, last_name)
        
        # If customer exists -> return customer instance
        if customer:
            print("\nKundendaten gefunden.")
            return customer
        
        # If customer does not exist -> create new customer instance
        customer = cls(0, first_name, last_name)
        
        # Add customer to DB
        customer.add_to_db()
        print("\nNeuer Kunde registriert.")
        
        return customer
        
class Item:
    """Template of an item (dish)
    """
    def __init__(self, id_:int, name:str, price:float, category_id:int) -> None:
        """Build an item instance

        Args:
            id_ (int): Unique item id
            name (str): Item name
            price (float): Price per Item
            category_id (int): Category the item belongs to e.g. "Pizzen"
        """
        self.id = id_
        self.name = name
        self.price = price
        self.category_id = category_id
        self.db = DBManager()
    
    def __repr__(self) -> str:
        """To print necessary item information

        Returns:
            str: Returns id / name / price of the item
        """
        return f"{self.id}. {self.name}" + (" " * (20 - len(self.name))) + f"{self.price:.2f}€"      
    
    def add_to_db(self) -> None:
        """Adds the item to SQLite DB
        """
        # Save item data in tuple
        data = (self.id, self.name, self.price, self.category_id)
        
        # SQL command for insertion of new item
        sql_insert_item = "INSERT INTO items (item_id, name, current_price, FK_category_id) VALUES (?, ?, ?, ?);"
    
        # Execute SQL command via DBManager
        self.db.insert_record(sql_insert_item, data)
        
    @staticmethod
    def get_items() -> list[object]:
        """Returns a list of all items in DB

        Returns:
            list[object]: Returns a list of item instances
        """
        
        # SQL command for selection of all items
        sql_get_items = "SELECT * FROM items"
        
        # Execute SQL command via DBManager and save all entries in list
        entries = DBManager().get_records(sql_get_items)
        
        # Create list of item instances
        items = []
        
        for entry in entries:
            item = Item(entry[0], entry[1], entry[2], entry[3]) # id, name, price, category_id
            items.append(item)
            
        return items
            
class Order:
    """Template of an order instance
    """
    def __init__(self) -> None:
        """To build an order instance

        Args:
            customer (object): Customer instance
        """
        self.id = 0
        self.date_time = ""
        self.item_dict = {} # TODO: __setitem__ / __getitem__  implementieren
        self.receipt = "" 
        self.customer = None
        self.db = DBManager()
        
    def add_items_and_date_time(self, order_dict:dict, date_time:str, items:list[object]) -> None:
        """Adds ordered items (instances) + quantity and date time to order instance

        Args:
            order_dict (dict): Dictionary with item id as key and quantity as value
            date_time (str): Date and time of order
            items (list[object]): List of item instances
        """
        self.date_time = date_time
        
        for item_id, quantity in order_dict.items():
            for item in items:
                if item_id == item.id:
                    self.item_dict[item] = quantity   
        
    def __repr__(self) -> str:
        return f"{self.id}. {self.customer.id}. {self.customer.first_name} {self.customer.last_name} {self.date_time} {self.item_dict}"
    
    def add_to_db(self) -> None:
        """Creates a new DB entry for order instance -> order + order item table
        """
        # 1. Insert order into DB -----------------------------------------------------------------------  
        # Create Tuple with order data
        order_data = (self.date_time, self.customer.id)
        
        # SQL command for insertion of new order
        sql_insert_order = f"INSERT INTO orders (date, FK_customer_id) VALUES (?, ?);"
        
        # Execute SQL command via DBManager
        self.id = self.db.insert_record(sql_insert_order, order_data)
            
            
        # 2. Insert order item into DB-----------------------------------------------------------------
        # Create list of Tuples with ordered item data
        order_item_data = []
        for item in self.item_dict:
            order_item_data.append((self.id, item.id, self.item_dict[item])) # FK_order_id, FK_item_id, quantity
        
        # SQL command for insertion of new order item
        sql_insert_order_item = f"INSERT INTO order_item (FK_order_id, FK_item_id, quantity) VALUES (?, ?, ?);"
        
        # Execute SQL command via DBManager for each item in order
        self.db.insert_records(sql_insert_order_item, order_item_data)

    def create_receipt(self) -> str:
        
        total_price = 0
        receipt = f""" 
 --------------------------------------------------
| Ihre Bestellung vom {self.date_time}          |
 --------------------------------------------------
| BestellNr: {self.id:11}   / KundenID: {self.customer.id:11} |
 --------------------------------------------------
| Nr.  | Gericht            | Anzahl | Einzelpreis |
 --------------------------------------------------
"""
        for item, quantity in self.item_dict.items():
            receipt += f"| {item.id:4} | {item.name:18} | {quantity:6} | {item.price:10.2f}€ |\n"
            total_price += item.price * quantity
        
        total_price = round(total_price, 2)
        
        receipt += """ --------------------------------------------------
| Gesamt:                     """ + ( " " * (18 - len( str( float(total_price) ) ) ) ) + f"""{float(total_price):.2f}€ |
 --------------------------------------------------
|                                                  |
| Vielen Dank für Ihren Besuch                     |
|                                                  |
| Beehren Sie uns bald wieder   ☻                  |
 --------------------------------------------------
"""
        # Save receipt to order instance
        self.receipt = receipt
        
        # Print receipt
        print(receipt)
              
    def save_receipt_to_file(self):
        """Saves the receipt to a text file
        """
        # Generate filename with order id
        filename = f"./receipts/receipt_order_{self.id}.txt"
        # Open file and write receipt to file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(self.receipt)
       

def main():
    pass

if __name__ == "__main__":
    main()