inventory = []

def register_item():
    print("\n--- Item Registration ---")
    name = str(input("Enter item name: ")).strip()
    if any(item["name"].lower() == name.lower() for item in inventory):
        print(f"❌ Error: An item with the name '{name}' already exists!")
        return  

    try:      
        quantity = int(input("Enter item quantity: "))
        price = float(input("Enter item price: ")) 
        category = str(input("Enter item category: "))
        condition = str(input("Enter item condition (new/used): ")).lower()
        notes = str(input("Enter additional notes: "))

        item_id = len(inventory) + 1
        
        item = {
            'id': item_id,
            'name': name,
            'quantity': quantity,
            'price': price,
            'category': category,
            'condition': condition,
            'notes': notes,
        }
        inventory.append(item)
        print(f"✅ Item '{name}' successfully registered with ID {item_id}!")

    except ValueError:
        print("❌ Error: Quantity and Price must be numbers. Registration cancelled.")

def list_items():
    print("\n--- Full Inventory ---")
    if not inventory:
        print("No items registered.")
        return
    for item in inventory:
        print(f"ID: {item['id']} | Name: {item['name']} | Qty: {item['quantity']} | Price: ${item['price']:.2f} | Cat: {item['category']}")

def search_item():
    print("\n--- Search ---")
    search_name = input("Enter name (or leave blank): ").lower()
    search_cat = input("Enter category (or leave blank): ").lower()
    
    results = [item for item in inventory
                  if (search_name in item['name'].lower() if search_name else False) or 
                     (search_cat in item['category'].lower() if search_cat else False)]
    
    if not results:
        print('No items found with these parameters.')
    else:
        for item in results:
            print(f"ID: {item['id']} - Name: {item['name']} ({item['category']})")

def add_or_remove():
    try:
        item_id = int(input("What is the item ID? "))
        operation = input("Do you want to add or remove? (add/rem): ").lower()
        amount_to_change = int(input("Quantity: "))

        for item in inventory:
            if item["id"] == item_id:
                if operation == "add":
                    item["quantity"] += amount_to_change
                    print(f"New total for {item['name']}: {item['quantity']}")
                elif operation == "rem":
                    if item["quantity"] >= amount_to_change:
                        item["quantity"] -= amount_to_change
                        print(f"New total for {item['name']}: {item['quantity']}")
                    else:
                        print("Error: Insufficient stock.")
                return
        print("ID not found.")
    except ValueError:
        print("Error: Please enter valid numerical values.")

def loan_registration():
    try:
        item_id = int(input("What is the ID of the item to be loaned? "))
        quantity = int(input("What is the desired quantity? "))

        for item in inventory:
            if item["id"] == item_id: 
                if quantity > 0 and item["quantity"] >= quantity:
                    item["quantity"] -= quantity
                    print(f"Loan of {quantity}x {item['name']} completed!")
                    return
                else:
                    print("Quantity unavailable or invalid.")
                    return
        print("ID not found.")
    except ValueError:
        print("Error: Invalid input.")