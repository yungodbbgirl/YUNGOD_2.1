import sys
from restaurant import Menu, Order


def main():
    menu = Menu()
    order = Order()

    menu.display()

    # Ask if user wants to order
    while True:
        start_order = input("Would you like to place an order? (y/n): ").strip().lower()
        if start_order in ['y', 'yes']:
            break
        elif start_order in ['n', 'no']:
            print("\nThank you for visiting! Goodbye.")
            sys.exit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    # Take order logic
    while True:
        try:
            choice = int(input("Enter the Item ID you wish to order: "))
            menu_item = menu.get_item(choice)
            if not menu_item:
                print("Invalid item ID. Please select a valid item from the menu.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numerical Item ID.")
            continue

        while True:
            try:
                quantity = int(input(f"Enter quantity for {menu_item.name}: "))
                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for quantity.")

        order.add_item(menu_item, quantity)

        while True:
            again = input("Would you like to order another item? (y/n): ").strip().lower()
            if again in ['y', 'yes', 'n', 'no']:
                break
            print("Please enter 'y' for yes or 'n' for no.")

        if again in ['n', 'no']:
            break

    # Print official receipt
    order.print_receipt()


if __name__ == "__main__":
    main()