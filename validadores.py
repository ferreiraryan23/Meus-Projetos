from core import inventory

def validate_by_id(item_id):
    """Checks if an ID exists in the inventory. Supports ID as int or numeric string."""
    try:
        item_id = int(item_id)
    except ValueError:
        return False
        
    return any(item["id"] == item_id for item in inventory)

def validate_by_name(name):
    # check if there is a item with the same name
    return any(item["name"].lower() == name.strip().lower() for item in inventory)