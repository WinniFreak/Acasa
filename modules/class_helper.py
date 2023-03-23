def assign_items_to_categories(categories:list[object], items:list[object]) -> list[object]:
    """Assign item instances to corresponding category instance

    Args:
        categories (list[object]): Category instances
        items (list[object]): Item instances

    Returns:
        list[object]: Category instances: Attribute item_list is filled with item instances
    """
    # Iterate over all category instances
    for category in categories:
        # Iterate over all item instances
        for item in items:
            # Check if FK_category_id from item matches category.id
            if item.category_id == category.id:
                # Insert item instance into category.item_list
                category.item_list.append(item)
    
    return categories

def show_menu(categories:list[object]) -> list[int]:
    """Prints menu to the console and returns a list of valid item ids

    Args:
        categories (list[object]): List of category instances with corresponding item instances in category.item_list

    Returns:
        list[int]: Valid item IDs
    """
    
    # Clears console and greets customer
    print("\033c")
    print("\nWillkommen im Acasa Restaurant\n------------------------------\n")
    
    # Create empty list for valid item ids
    valid_ids = []
    
    # Iterate over all category instances
    for category in categories:
        # Print category title and underscores
        print(category)
        print("-" * len(category.title))
        
        # Iterate over all items for the category
        for item in category.item_list:
            # Print item ID / name / price
            print(item)
            # Append item ID to list of valid IDs
            valid_ids.append(item.id)
        
        print()

    return valid_ids


def main():
    pass

if __name__ == "__main__":
    main()