from core import inventory

def generate_category_report():
    '''Function to generate a report of items grouped by category'''
    
    if not inventory:
        print("The inventory is empty.")
        return

    categories = {}
    for item in inventory:
        cat = item['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(item)
    
    print("\n=== REPORT BY CATEGORY ===")
    for category, items in categories.items():
        print(f"\n📂 CATEGORY: {category.upper()}")
        print("-" * 30)
        for item in items:
            print(f"ID: {item['id']} | Name: {item['name']}")
            print(f"Quantity: {item['quantity']} | Price: ${item['price']}")
            print(f"Condition: {item['condition']} | Notes: {item['notes']}")
            print("-" * 15)