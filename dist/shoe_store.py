

class StationeryStore:
    def __init__(self):
        # Pre-made inventory for stationery items
        self.inventory = {
            "Notebook": {"price": 30, "quantity": 50},
            "Pen": {"price": 10, "quantity": 100},
            "Pencil": {"price": 7, "quantity": 150},
            "Eraser": {"price": 10, "quantity": 80},
            "Ruler": {"price": 15, "quantity": 40},
            "Marker": {"price": 20, "quantity": 30},
            "Highlighter": {"price": 25, "quantity": 25},
            "Stapler": {"price": 35, "quantity": 15},
            "Scissors": {"price": 40, "quantity": 20},
            "Glue Stick": {"price": 25, "quantity": 35},
            "Paper Clips (Pack of 50)": {"price": 75, "quantity": 20},
            "Sticky Notes": {"price": 25, "quantity": 25},
            "Calculator": {"price": 120, "quantity": 10},
            "Whiteboard": {"price": 400, "quantity": 5},
            "Sketchbook": {"price": 40, "quantity": 12},
            "Paint Set": {"price": 100, "quantity": 10},
            "Drawing Compass": {"price": 80, "quantity": 15},
            "Protractor": {"price": 10, "quantity": 25},
            "Folder": {"price": 20, "quantity": 50},
            "Binder": {"price": 30, "quantity": 10}
        }
        # Customer list and purchase history
        self.testdict = {'A': [{'item': 'Pen', 'quantity': 1, 'total_price': 10}, {'item': 'Pencil', 'quantity': 2, 'total_price': 14}], 'B': [{'item': 'Stapler', 'quantity': 2, 'total_price': 70}]}
        self.customers = {}
        self.purchase_history = {}

    def add_item(self, name, price, quantity): #Adds item to the inventory
        if name in self.inventory:
            self.inventory[name]["quantity"] += quantity
        else:
            self.inventory[name] = {"price": price, "quantity": quantity}
        print(f"Added {quantity} {name}(s) to the inventory.")

    def show_inventory(self): #Prints the inventory 
        if not self.inventory:
            print("The inventory is empty.")
            return
        print("\nAvailable Stationery Items:")
        print("{:<30} {:<10} {:<10}".format("Name", "Price", "Quantity"))
        print("-" * 50)
        for name, details in self.inventory.items():
            print("{:<30} {:<10} {:<10}".format(name, details["price"], details["quantity"]))
        print()

    def search_item(self, name): #searches the item from the inventory by name
        if name in self.inventory:
            details = self.inventory[name]
            print(f"\n{name} found in inventory:")
            print(f"Price: ${details['price']}, Quantity: {details['quantity']}\n")
        else:
            print(f"{name} not found in the inventory.")

    def delete_item(self, name): #Deletes the item from the inventory by name
        if name in self.inventory:
            del self.inventory[name]
            print(f"{name} has been removed from the inventory.")
        else:
            print(f"{name} not found in the inventory.")

    def edit_item_details(self, name): #Edits an item's price and quantity 
        if name not in self.inventory:
            print(f"{name} not found in the inventory.")
            return
        print(f"\nCurrent details for {name}:")
        print(f"Price: ${self.inventory[name]['price']}, Quantity: {self.inventory[name]['quantity']}")
        try:
            new_price = float(input("»Enter new price (or press »Enter to keep current price): ") or self.inventory[name]['price'])
            new_quantity = int(input("»Enter new quantity (or press »Enter to keep current quantity): ") or self.inventory[name]['quantity'])
            self.inventory[name] = {"price": new_price, "quantity": new_quantity}
            print(f"{name} details have been updated.")
        except ValueError:
            print("Invalid input. Please »Enter valid numbers.")

    def clear_inventory(self): #Clears the inventory
        confirm = input("Are you sure you want to clear the entire inventory? (yes/no): ").strip().lower()
        if confirm == "yes":
            self.inventory.clear()
            print("Inventory has been cleared.")
        else:
            print("Operation canceled.")

    def register_customer(self, name, email, phone): #Registers customers with name, email and phone number
        if email in self.customers:
            print(f"Customer with email {email} is already registered.")
            return
        self.customers[email] = {"name": name, "phone": phone}
        self.purchase_history[email] = []
        print(f"Customer {name} has been registered successfully.")

    def view_customers(self): #Display the list of registered customers
        if not self.customers:
            print("No customers registered yet.")
            return
        print("\nRegistered Customers:")
        print("{:<30} {:<30} {:<15}".format("Name", "Email", "Phone"))
        print("-" * 75)
        for email, details in self.customers.items():
            print("{:<30} {:<30} {:<15}".format(details["name"], email, details["phone"]))
        print()

    def remove_customer(self, email): #Remove a customer from the list
        if email in self.customers:
            del self.customers[email]
            del self.purchase_history[email]
            print(f"Customer with email {email} has been removed.")
        else:
            print(f"No customer found with email {email}.")

    def purchase_item(self, name, quantity): #Purchasing an item
        if name not in self.inventory:
            print("Item not found in the inventory.")
            return

        if self.inventory[name]["quantity"] < quantity:
            print(f"Not enough stock for {name}. Available: {self.  inventory[name]['quantity']}")
            return

        total_price = self.inventory[name]["price"] * quantity
        self.inventory[name]["quantity"] -= quantity
        if self.inventory[name]["quantity"] == 0:
            del self.inventory[name]
        print(f"Successfully purchased {quantity} {name}(s) for $   {total_price:.2f}.")


    def view_customer_purchase_history(self, email): #View the purchase history of a specific customer
        if email not in self.customers:
            print("Customer not registered.")
            return

        if not self.purchase_history[email]:
            print(f"No purchase history for {self.customers[email]['name']}.")
            return

        print(f"\nPurchase History for {self.customers[email]['name']}:")
        print("{:<20} {:<10} {:<10}".format("Item", "Quantity", "Total Price"))
        print("-" * 50)
        for record in self.purchase_history[email]:
            print("{:<20} {:<10} {:<10.2f}".format(record["item"], record["quantity"], record["total_price"]))
        print()

    def purchase_item_by_customer(self, email, item_name, quantity): #Allow a registered customer to purchase an item.
        if email not in self.customers:
            print("Customer not registered. Please register first.")
            return

        if item_name not in self.inventory:
            print(f"Item {item_name} not found in the inventory.")
            return

        if self.inventory[item_name]["quantity"] < quantity:
            print(f"Not enough stock for {item_name}. Available: {self.inventory[item_name]['quantity']}")
            return

        total_price = self.inventory[item_name]["price"] * quantity
        self.inventory[item_name]["quantity"] -= quantity
        if self.inventory[item_name]["quantity"] == 0:
            del self.inventory[item_name]

        # Record purchase in the customer's history
        self.purchase_history[email].append({"item": item_name, "quantity": quantity, "total_price": total_price})
        print(f"{self.customers[email]['name']} purchased {quantity} {item_name}(s) for ${total_price:.2f}.")

    def test(self, x): #Nevermind
        print(x) 
        print(self.purchase_history)
    
    def view_all_purchases(self): # Display all items purchased by each customer
        if not self.purchase_history:
            print("No purchases made yet.")
            return

        print("\nAll Customer Purchases:")
        for email, purchases in self.purchase_history.items():
            print(f"\nPurchases for {self.customers[email]['name']} (Email: {email}):")
            if not purchases:
                print("  No purchases found.")
                continue

            print("{:<25} {:<10} {:<10} {:<10}".format("Item", "Quantity", "Price", "Total"))
            print("-" * 50)
            for purchase in purchases:
                item = purchase["item"]
                quantity = purchase["quantity"]
                price = self.inventory[item]["price"]
                total_price = purchase["total_price"]
                print("{:<25} {:<10} {:<10} {:<10.2f}".format(item, quantity, price, total_price))
        print()


def main(): #Calling functions
    store = StationeryStore()
    menu = """Stationery Store Menu:
1. Show Inventory
2. Add Item to Inventory
3. Purchase Item
4. Search for an Item
5. Delete Item from Inventory
6. Edit Item Details
7. Clear Inventory
8. Register Customer
9. View Registered Customers
10. Remove Customer
11. Customer Purchase Item
12. View Customer Purchase History
13. View All Purchases
14. Exit"""
    print(menu)

    while True:
        print("\n⁘ Enter 0 to get the menu ⁘")
        choice = input("»Enter your choice (1-14): ")

        if choice == "0":
            print(menu)
        elif choice == "1":
            store.show_inventory()
        elif choice == "2":
            name = input("\n»Enter item name: ")
            try:
                price = float(input("»Enter item price: "))
                quantity = int(input("»Enter item quantity: "))
                store.add_item(name, price, quantity)
            except ValueError:
                print("Invalid input. Please »Enter valid numbers for price and quantity.")
        elif choice == "3":
            name = input("\n»Enter item name to purchase: ")
            try:
                quantity = int(input("»Enter quantity to purchase: "))
                store.purchase_item(name, quantity)
            except ValueError:
                print("Invalid input. Please »Enter a valid number for quantity.")
        elif choice == "4":
            name = input("\n»Enter item name to search: ")
            store.search_item(name)
        elif choice == "5":
            name = input("\n»Enter item name to delete: ")
            store.delete_item(name)
        elif choice == "6":
            name = input("\n»Enter item name to edit: ")
            store.edit_item_details(name)
        elif choice == "7":
            store.clear_inventory()
        elif choice == "8":
            name = input("\n»Enter customer name: ")
            email = input("\n»Enter customer email: ")
            phone = input("\n»Enter customer phone: ")
            store.register_customer(name, email, phone)
        elif choice == "9":
            store.view_customers()
        elif choice == "10":
            email = input("\n»Enter customer email to remove: ")
            store.remove_customer(email)
        elif choice == "11":
            email = input("\n»Enter customer email: ")
            item_name = input("\n»Enter item name: ")
            try:
                quantity = int(input("»Enter quantity: "))
                store.purchase_item_by_customer(email, item_name, quantity)
            except ValueError:
                print("Invalid input. Please »Enter a valid number for quantity.")
        elif choice == "12":
            email = input("\n»Enter customer email: ")
            store.view_customer_purchase_history(email)
        elif choice == "13":
            store.view_all_purchases()
        elif choice == "14":
            print("\nThank you for visiting the stationery store!")
            break
        elif choice =="test":
            store.test('exe')
        else:
            print("Invalid choice. Please try again.")
        

if __name__ == "__main__":
    main()