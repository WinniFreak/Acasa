# Imports 
import sqlite3
import db.config
import os.path

class DBManager:
    """Class to manage the connection to the SQLite DB and execute SQL queries
    """
    
    def __init__(self) -> None:
        """Build a DBManager instance to establish a connection to SQLite DB"""
        
        # print(db.config.DB_FILE_PATH)
        
        # Get DB file path from config file
        DB_FILE_PATH = db.config.DB_FILE_PATH
        
        
        # Check if DB file exists
        if os.path.isfile(DB_FILE_PATH):
           # Establish connection to DB
           self.conn = sqlite3.connect(DB_FILE_PATH)
           self.cursor = self.conn.cursor()
           # print("DB connection established!")
        else:
            print("DB file not found! Check DB_FILE_PATH in 'config.json' file.")
            exit()
                
        
    def get_record(self, sql:str, data:tuple = None) -> tuple:
        """Makes a query to the DB and returns the first record

        Args:
            sql (str): SQL query provided by class method
            data (tuple, optional): Data tuple provided by class method - Defaults to None.

        Returns:
            tuple: Returns the first record
        """
       
        if data: # If data is provided, like WHERE '...' = ?
            self.cursor.execute(sql, data)
        else:
            self.cursor.execute(sql)
        
        # Return the first record
        return self.cursor.fetchone()
        
    def get_records(self, sql:str, data:tuple = None) -> list[tuple]:
        """Makes a query to the DB and returns all records

        Args:
            sql (str): SQL query provided by class method
            data (tuple, optional): Data tuple provided by class method - Defaults to None.

        Returns:
            list [tuple]: Returns all records
        """
        
        if data: # If data is provided, like WHERE '...' = ?
            self.cursor.execute(sql, data)
        else:
            self.cursor.execute(sql)
            
        # Return all records
        return self.cursor.fetchall()
    
    def insert_record(self, sql:str, data:tuple = None) -> int:
        """Makes a query to the DB to insert a record and returns ID of this record

        Args:
            sql (str): SQL query provided by class method
            data (tuple, optional): Data tuple provided by class method - Defaults to None.

        Returns:
            int: Returns the last row ID
        """
        
        with self.conn:
            if data:
                self.cursor.execute(sql, data)
            else:
                self.cursor.execute(sql)
                
        # Return the last row ID
        return self.cursor.lastrowid
    
    def insert_records(self, sql:str, data:list[tuple]) -> None:
        """Makes a query to the DB to insert multiple records

        Args:
            sql (str): SQL query provided by class method
            data (list [tuple]): Data list provided by class method
        """
        
        with self.conn:
            self.cursor.executemany(sql, data)


def show_all_orders():
    # Create DBManager instance
    db = DBManager()

    # Clear console
    print("\033c")

    # SQL Statement to collect customers with name and id from DB
    sql_customers = """SELECT DISTINCT c.first_name, c.last_name, c.customer_id
                       FROM customers AS c
                       JOIN orders as o
                       on c.customer_id = o.FK_customer_id;"""
                            
    # SQL Statement to collect orders with id and date from DB
    sql_orders = """SELECT order_id, date
                    FROM orders
                    WHERE FK_customer_id = ?;"""
                    
    # SQL Statement to collect ordered items with id, name, quantity and price from DB
    sql_order_items = """SELECT i.name, oi.quantity, i.current_price
                         FROM items AS i 
                         JOIN order_item AS oi
                         ON i.item_id = oi.FK_item_id
                         WHERE oi.FK_order_id = ?;"""

    # Get all customers
    customers = db.get_records(sql_customers)

    # Iterate over all customers
    for customer in customers:
        
        # Print customer information
        customer_information = f"{customer[0]} {customer[1]}" # first_name, last_name
        print(customer_information)
        print('-' * len(customer_information))
        
        # Get all orders for customer id
        orders = db.get_records(sql_orders, (customer[2],)) # customer_id
        
        # Iterate over all orders from customer
        for order_counter, order in enumerate(orders, start=1):
            
            # Print order information
            order_information = f"{order_counter}. Order on {order[1]}" # n-th order from customer, date
            print(order_information) 
            print('-' * len(order_information))
            
            # Get all ordered items for order id
            items = db.get_records(sql_order_items, (order[0],)) # order_id
            
            # Iterate over all ordered items from order
            for item_counter, item in enumerate(items, start=1):
                
                # Print item information
                item_information = f"{item_counter}. {item[0]:20} ({item[1]}x) {item[2]:.2f}€" # n-th item from order, name, quantity, price
                print(item_information)
                
            print()
            
        print()

def main():
    # Check if DB connection is working
    db_manager = DBManager()
    # with db_manager.conn: 
    #     rows = db_manager.cursor.execute("SELECT * FROM customers")
    #     for row in rows:
    #         print(row)
            
    # # Check if get_record() is working
    # item = db_manager.get_record("SELECT * FROM items WHERE item_id = ?", (102,)) # item with id = 102
    # print(item)
    # item = db_manager.get_record("SELECT * FROM items") # first item from items table
    # print(item)
    
    
    
    
 
if __name__ == "__main__":
    main()
    