from datetime import datetime

def select_option() -> int:
    print("\033c")
    print(f"Welcome to Acasa Restaurant\n{'-' * 27}\n")
    print(f"1. New order\n2. Show all orders from the DB\n3. Menu Management\n")
    
    while True:
        try:
            choice = int(input("> "))
            if choice in [1,2]:
                return choice
            elif choice == 3:
                print("> Menu Management is not implemented yet.")
            else:
                raise ValueError
        except ValueError:
            print("> Bitte geben Sie eine gültige Zahl ein.")
        
def get_customer_info() -> dict:
    """To get personal iformation about the customer

    Returns:
        dict: First and last name of the user
    """
    
    print("\nZum Fortfahren bitte persönliche Daten eingeben.")
    
    
    customer_info = {"first_name": "Vorname: ",
                     "last_name": "Nachname: "}
    
    for key, value in customer_info.items():
        try:
            customer_info[key] = input(value).strip().title()
            # print(customer_info[key])
        except ValueError:
            print("Bitte geben Sie einen gültigen Namen ein.")
    return customer_info
         
def get_order(valid_ids:list) -> dict:
    """Gets the order from customer and returns a dict with ordered dish ids and their quantity. Exit input phase with '0'.

    Args:
        valid_ids (list): List with valid dish ids

    Returns:
        dict: Dictionary with ordered dish ids as keys and their quantity as values
    """
    print("Was möchten Sie bestellen?")
    
    order_dict = {}
    
    while True:
        try:
            id = int(input("> "))
            if id in valid_ids:
                if id in order_dict:
                    order_dict[id] += 1
                else:
                    order_dict[id] = 1
            elif id == 0:
                break
            else:
                print(f"> {id} bieten wir leider nicht an.")
        except ValueError:
            print("Bitte geben Sie eine gültige Bestellnummer ein.")
        finally:
            date_time =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       
    return order_dict, date_time

# TODO - add validation for name : allow spaces 
def ValidName(name):
    if len(name) > 3 and name.isalpha():
        return True
    else:
        return False


def main():
    print(select_option())
    
    
    # customer_info = get_customer_info()
    # print(customer_info)

    
    
if __name__ == "__main__":
    main()