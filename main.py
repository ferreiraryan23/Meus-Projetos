from core import (
    register_item, 
    list_items, 
    search_item, 
    add_or_remove, 
    loan_registration,
    inventory  
)

def menu():
    while True:
        print("\n=== INVENTORY SYSTEM ===")
        print("1. Register Item")
        print("2. List Items")
        print("3. Search Item")
        print("4. Add/Remove Stock")
        print("5. Record Loan")
        print("6. View Total Stock Value")
        print("0. Exit")
        
        choice = input("Choose an option: ").strip()

        if choice == "1":
            register_item()
        elif choice == "2":
            list_items()
        elif choice == "3":
            search_item()
        elif choice == "4":
            add_or_remove()
        elif choice == "5":
            loan_registration()
        elif choice == "6":
            total_value = sum(item['price'] * item['quantity'] for item in inventory)
            print(f"Total Stock Value: ${total_value:,.2f}")
        elif choice == "0": 
            print("Exiting system... Goodbye!")
            break
        else: 
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    menu()