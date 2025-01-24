class VendingMachine:
    def __init__(self):
        # activate the vending machine with prefined items
        # Each item has unique code, name, price, and stock
        self.items = {
            'A1': {'name': 'Chips', 'price': 1.50, 'stock': 5},
            'A2': {'name': 'Soda', 'price': 1.25, 'stock': 0},
            'A3': {'name': 'Candy', 'price': 0.75, 'stock': 10},
            'B1': {'name': 'Chocolate Bar', 'price': 1.00, 'stock': 3},
            'B2': {'name': 'Gum', 'price': 0.50, 'stock': 20},
            'B3': {'name': 'Cookies', 'price': 1.75, 'stock': 2},
            'C1': {'name': 'Juice', 'price': 1.50, 'stock': 4},
            'C2': {'name': 'Water', 'price': 1.00, 'stock': 6},
            'C3': {'name': 'Energy Drink', 'price': 2.00, 'stock': 1},
            'D1': {'name': 'Granola Bar', 'price': 1.25, 'stock': 5},
        }

    def display_items(self):
        # Displays the available items with their prices and stock 
        # items out of stock are clearly labeled
        """Displays the available items with their prices and stock status."""
        print("\nAvailable Items")
        print("----------------")
        for code, item in self.items.items():
            stock_status = f"stock'if item['stock'] == 0 else f"Stock: {item['stock']}"
            print(f"{code}: {item['name']} - ${item['price']} ({stock_status})")

    def purchase_item(self, code, money_inserted):
        """Handles the purchase of an item by code and the money inserted."""
        #Parameters:
        # code (str): The uniqe code of the item
        # money_inserted (float): the amount of money inserted by the user'''
        if code in self.items:
            item = self.items[code]
            if item['stock'] > 0:
                if money_inserted >= item['price']:
                    change = round(money_inserted - item['price'], 2)
                    item['stock'] -= 1
                    print(f"\nYou have purchased: {item['name']}. Your change is ${change}. Thank you!")
                else:
                    print(f"\nInsufficient funds. {item['name']} costs ${item['price']}, but you only inserted ${money_inserted}.")
            else:
                print("\nSorry, this item is out of stock.")
        else:
            print("\nInvalid item code. Please try again.")

if __name__ == "__main__":
    vending_machine = VendingMachine()

    while True:
        vending_machine.display_items()
        user_input = input("\nEnter the item code to purchase or 'exit' to quit: ").strip().upper()

        if user_input == 'EXIT':
            print("\nThank you for using Hassan's vending machine. Goodbye!")
            break
        
        if user_input in vending_machine.items:
            try:
                money_inserted = float(input("Enter the amount of money you are inserting: "))
                vending_machine.purchase_item(user_input, money_inserted)
            except ValueError:
                print("\nInvalid input. Please enter a valid numerical amount for the money.")
        else:
            print("\nInvalid code entered. Please try again.")
