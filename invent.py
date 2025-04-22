class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        print(f"Added {quantity} {item_name}(s). Current stock: {self.items[item_name]}")

    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            if self.items[item_name] >= quantity:
                self.items[item_name] -= quantity
                print(f"Removed {quantity} {item_name}(s). Current stock: {self.items[item_name]}")
            else:
                print(f"Not enough {item_name}(s) in stock. Current stock: {self.items[item_name]}")
        else:
            print(f"{item_name} not found in inventory.")

    def check_availability(self, item_name):
        if item_name in self.items:
            print(f"Current stock of {item_name}: {self.items[item_name]}")
        else:
            print(f"{item_name} not found in inventory.")

    def display_inventory(self):
        print("\nCurrent Inventory:")
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")


def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management Options:")
        print("1. Add item to inventory")
        print("2. Remove item from inventory")
        print("3. Check item availability")
        print("4. Display current inventory")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            inventory.add_item(item_name, quantity)
        elif choice == "2":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            inventory.remove_item(item_name, quantity)
        elif choice == "3":
            item_name = input("Enter item name: ")
            inventory.check_availability(item_name)
        elif choice == "4":
            inventory.display_inventory()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()
