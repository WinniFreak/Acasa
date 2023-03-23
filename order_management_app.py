# Import libraries
import os
from pathlib import Path

# Import classes
from db.classes import Category, Customer, Item, Order

# Import modules
from modules.user_inputs import get_customer_info, get_order, select_option
from modules.class_helper import assign_items_to_categories, show_menu
from db.db_manager import show_all_orders

# Change enty point to application folder
os.chdir(Path(__file__).parent)

def main():
    # Let user choose between 1. new order or 2. show orders 3. menu_management is not implemented yet
    choice = select_option()
    
    match choice:
        case 3:
            pass

        
        case 2:
            # Prints all orders from DB to console
            show_all_orders()
            
        case 1:
             # Create a list of category instances
            categories = Category.get_categories()
            
            # Create a list of item instances
            items = Item.get_items()
            
            # Assign items to corresponding category
            categories = assign_items_to_categories(categories, items)
            
            # Print menu to console and get valid item IDs
            valid_ids = show_menu(categories)
            
            # Get item IDs from user input and save them with their quantity in a dictionary + get date and time
            order_dict, date_time = get_order(valid_ids)
            
            
            
            # Check if anything was ordered if not -> exit program ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            if not order_dict:
                print("\nKonnten wir Sie nicht von unserer Speisekarte überzeugen?\n")
                exit()
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            
            
            
            # Create blank order instance
            order = Order()
            
            # Assign item instances + quantity and date_time to order instance 
            order.add_items_and_date_time(order_dict, date_time, items)
            # print(order.item_dict)
            
            # Get customer name from input
            customer_info = get_customer_info()
            
            # Create a customer instance
            customer = Customer.get_or_create_customer(customer_info["first_name"], customer_info["last_name"])
            
            # Assign customer instance to order instance
            order.customer = customer
            
            # Add order to DB
            order.add_to_db()
            
            # Create / print receipt
            order.create_receipt()
            
            # Save order to file
            order.save_receipt_to_file()
            
        case _:
            print("Something went wrong.")
    
    
if __name__ == "__main__":
    main()