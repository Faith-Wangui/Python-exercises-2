class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
            print(f"Updated {name} quantity to {self.items[name]}.")
        else:
            self.items[name] = quantity
            print(f"Added {name} with quantity {quantity}.")

    def get_item(self, name):
        if name in self.items:
            print(f"{name}: {self.items[name]} in stock.")
        else:
            print(f"{name} is not in the inventory.")

    def total_quantity(self):
        total = sum(self.items.values())
        print(f"Total inventory quantity: {total}")

# Example usage
inventory = Inventory()

while True:
    print("\nInventory System:\n1. Add/Update Item\n2. Get Item Info\n3. Show Total Quantity\n4. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        name = input("Enter item name:Books ")
        quantity = int(input("Enter quantity:10 "))
        inventory.add_item(name, quantity)
    elif choice == '3':
        name = input("Enter item name:Laptops ")
        inventory.get_item(name)
    elif choice == '4':
        inventory.total_quantity()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
