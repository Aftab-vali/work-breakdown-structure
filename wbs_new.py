class Starbucks:
    def __init__(self):
        # Initialize dictionaries to store items and their prices
        self.items = {}
        self.prices = {}

    def add_item(self, item, price):
        # Add item and its price to the items dictionary
        self.items[item] = price

    def update_item(self, item, price):
        # Update item's price
        if item in self.items:
            self.items[item] = price
            print(f"{item} updated successfully.")
        else:
            print("Item not found in the menu.")

    def delete_item(self, item):
        # Delete item from the menu
        if item in self.items:
            del self.items[item]
            print(f"{item} deleted successfully.")
        else:
            print("Item not found in the menu.")

    def display_menu(self):
        # Display current menu
        print("Current Menu:")
        for item, price in self.items.items():
            print(f"{item}: ${price}")

    def process_order(self):
        # Phase 3: Process the order
        selected_items = self.select_items()
        total_bill = self.calculate_bill(selected_items)

        print("Thank you for visiting StarBucks! ☕️🌟")
        self.display_items(selected_items)

        # Calculate and display CGST and SGST
        cgst_rate = 0.09 / 2
        cgst = round(total_bill * cgst_rate, 2)
        sgst = round(total_bill * cgst_rate, 2)

        print('CGST (9%): $', cgst)
        print('SGST (9%): $', sgst)

        # Add CGST and SGST to the total bill
        total_bill += (cgst + sgst)
        print("Your total bill is: $", round(total_bill, 2))

    def select_items(self):
        # Phase 1: Display available items
        print("Welcome to StarBucks! ☕️🌟")
        print("Here are the available items:")
        for item, price in self.items.items():
            print(f"{item}: ${price}")

        selected_items = []  # List to store selected items


        # Phase 2: Select items to buy
        while True:
            item = input("Enter the item you want to buy (or 'done' to finish) (or 'update' to change the order): ")
            if item.lower() == 'update':
                selected_items = self.update(selected_items)
            elif item.lower() == 'done':
                break
            elif item in self.items:
                selected_items.append(item)  # Add selected item to the list
            else:
                print("Item not found. Please select from the available items.")

        return selected_items

    def update(self, selected_items):
        previous_item = input('Enter the item you want to update: ')
        if previous_item in selected_items:
            updated_item = input('Enter the new item: ')
            selected_items[selected_items.index(previous_item)] = updated_item
            print(f"{previous_item} updated to {updated_item}.")
        else:
            print("Item not found in the order.")
        return selected_items

    def display_items(self, selected_items):
        # Display selected items and their prices
        print('-------->BILLING ITEMS <---------')
        print("Your order:")
        for item in selected_items:
            print(f"{item}: ${self.items[item]}")

    def calculate_bill(self, selected_items):
        # Calculate total bill based on selected items
        total_bill = sum(self.items[item] for item in selected_items)
        return total_bill


def authenticate_user():
    # Read usernames and passwords from the credentials file
    credentials = {}
    with open('credentials.txt', 'r') as file:
        for line in file:
            username, password = line.strip().split(',')
            credentials[username] = password

    # Prompt user for username and password
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in credentials and credentials[username] == password:
            print(f"Welcome, {username}! Authentication successful!")
            return True, username  # Return username upon successful authentication
        else:
            print("Invalid username or password. Please try again.")


def main_menu(starbucks, username):
    while True:
        print(f"\nMain Menu for {username}:")
        print("1. Add Item to Menu")
        print("2. Update Item in Menu")
        print("3. Delete Item from Menu")
        print("4. View Menu")
        print("5. Process Order")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item name: ")
            price = float(input("Enter the price: "))
            starbucks.add_item(item, price)
            print("Item added successfully.")
        elif choice == '2':
            item = input("Enter the item name to update: ")
            price = float(input("Enter the new price: "))
            starbucks.update_item(item, price)
        elif choice == '3':
            item = input("Enter the item name to delete: ")
            starbucks.delete_item(item)
        elif choice == '4':
            starbucks.display_menu()
        elif choice == '5':
            starbucks.process_order()
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

        # Ask if the user wants to return to the main menu
        return_menu = input("Return to main menu? (yes/no): ")
        if return_menu.lower() != 'yes':
            break



if __name__ == "__main__":
    # Authenticate user before proceeding
    authenticated, username = authenticate_user()


    if authenticated:
        # If authentication is successful, proceed with the order
        starbucks = Starbucks()
        starbucks.add_item("Coffee", 2.25)
        starbucks.add_item("Latte", 3.95)
        starbucks.add_item("Cappuccino", 3.65)
        starbucks.add_item('Mocha', 4.15)
        starbucks.add_item('Americano', 2.95)
        starbucks.add_item('Espresso', 2.25)
        starbucks.add_item('Tea', 3)
        starbucks.add_item('Pepsi', 1.9)
        starbucks.add_item('Thums Up', 2)
        starbucks.add_item('Dark Chocolate', 5)

        main_menu(starbucks, username)
