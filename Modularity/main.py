import sys
from config import MENU
from menu import display_menu
from order import get_user_order, calculate_order_totals, print_receipt

def main():
    display_menu(MENU)

    while True:
        start_order = input("Would you like to place an order? (y/n): ").strip().lower()
        if start_order in ['y', 'yes']:
            break
        elif start_order in ['n', 'no']:
            print("\nThank you for visiting! Goodbye.")
            sys.exit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    cart = get_user_order(MENU)
    subtotal, discount, grand_total = calculate_order_totals(cart)
    print_receipt(cart, subtotal, discount, grand_total)

if __name__ == "__main__":
    main()