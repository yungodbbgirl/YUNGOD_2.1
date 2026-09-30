from config import DISCOUNT_RATE, DISCOUNT_THRESHOLD


def get_user_order(menu_dict):
    cart = []

    while True:
        try:
            choice = int(input("Enter the Item ID you wish to order: "))
            if choice not in menu_dict:
                print("Invalid item ID. Please select a valid item from the menu.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numerical Item ID.")
            continue

        while True:
            try:
                quantity = int(input(f"Enter quantity for {menu_dict[choice]['name']}: "))
                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for quantity.")

        cart.append({
            "name": menu_dict[choice]["name"],
            "price": menu_dict[choice]["price"],
            "quantity": quantity
        })

        while True:
            again = input("Would you like to order another item? (y/n): ").strip().lower()
            if again in ['y', 'yes', 'n', 'no']:
                break
            print("Please enter 'y' for yes or 'n' for no.")

        if again in ['n', 'no']:
            break

    return cart


def calculate_order_totals(cart):
    subtotal = 0.0
    for item in cart:
        item["total_price"] = item["price"] * item["quantity"]
        subtotal += item["total_price"]

    discount = subtotal * DISCOUNT_RATE if subtotal >= DISCOUNT_THRESHOLD else 0.0
    grand_total = subtotal - discount

    return subtotal, discount, grand_total


def print_receipt(cart, subtotal, discount, grand_total):
    print("\n" + "*" * 48)
    print("             OFFICIAL RECEIPT             ")
    print("           BB.GIRL'S RESTAURANT           ")
    print("*" * 48)
    print(f"{'Item':<18} {'Qty':<5} {'Price':<11} {'Total':>10}")
    print("-" * 48)

    for item in cart:
        print(f"{item['name']:<18} {item['quantity']:<5} PHP {item['price']:<7.2f} PHP {item['total_price']:>7.2f}")

    print("-" * 48)
    print(f"{'Subtotal:':<32} PHP {subtotal:>9.2f}")
    if discount > 0:
        print(f"{'Discount (10% over PHP 500):':<32} -PHP {discount:>8.2f}")
    print(f"{'GRAND TOTAL:':<32} PHP {grand_total:>9.2f}")
    print("*" * 48)
    print("        Salamat po for your order!        ")
    print("             Have a great day!            \n")