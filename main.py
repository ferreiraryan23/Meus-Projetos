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
        
        choice = input("Choose an option: ")

        if choice == "1":
            from core import register_item
            register_item()
        elif choice == "2":
            from core import list_items
            list_items()
        elif choice == "3":
            from core import search_item
            search_item()
        elif choice == "4":
            from core import add_or_remove
            add_or_remove()
        elif choice == "5":
            from core import loan_registration
            loan_registration()
        elif choice == "6":
            from core import inventory
            total_value = sum(i['price'] * i['quantity'] for i in inventory)
            print(f"Total Stock Value: ${total_value:.2f}")
        elif choice == "0": 
            print("Exiting system...")
            break
        else: 
            print("Invalid option.")

if __name__ == "__main__":
    menu()