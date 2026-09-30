import sys


class MenuItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price


class Menu:
    def __init__(self):
        self.items = {
            1: MenuItem(1, "Burger Deluxe", 149.00),
            2: MenuItem(2, "Crispy Fries", 69.00),
            3: MenuItem(3, "Fountain Drink", 49.00),
            4: MenuItem(4, "Chicken Combo", 219.00),
            5: MenuItem(5, "Ice Cream Cone", 35.00)
        }

    def display(self):
        print("\n" + "="*45)
        print("        WELCOME TO BB.GIRL'S RESTAURANT      ")
        print("="*45)
        print(f"{'ID':<5} {'Item':<22} {'Price':>15}")
        print("-" * 45)
        for item in self.items.values():
            print(f"{item.item_id:<5} {item.name:<22} PHP {item.price:>9.2f}")
        print("="*45 + "\n")

    def get_item(self, item_id):
        return self.items.get(item_id)


class OrderItem:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity

    def calculate_total(self):
        return self.menu_item.price * self.quantity


class Order:
    DISCOUNT_RATE = 0.10
    DISCOUNT_THRESHOLD = 500.00

    def __init__(self):
        self.items = []

    def add_item(self, menu_item, quantity):
        self.items.append(OrderItem(menu_item, quantity))

    def calculate_subtotal(self):
        return sum(item.calculate_total() for item in self.items)

    def calculate_discount(self):
        subtotal = self.calculate_subtotal()
        return subtotal * self.DISCOUNT_RATE if subtotal >= self.DISCOUNT_THRESHOLD else 0.0

    def calculate_grand_total(self):
        return self.calculate_subtotal() - self.calculate_discount()

    def print_receipt(self):
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        grand_total = self.calculate_grand_total()

        print("\n" + "*"*48)
        print("             OFFICIAL RECEIPT             ")
        print("           BB.GIRL'S RESTAURANT           ")
        print("*"*48)
        print(f"{'Item':<18} {'Qty':<5} {'Price':<11} {'Total':>10}")
        print("-" * 48)

        for order_item in self.items:
            print(
                f"{order_item.menu_item.name:<18} "
                f"{order_item.quantity:<5} "
                f"PHP {order_item.menu_item.price:<7.2f} "
                f"PHP {order_item.calculate_total():>7.2f}"
            )

        print("-" * 48)
        print(f"{'Subtotal:':<32} PHP {subtotal:>9.2f}")
        if discount > 0:
            print(f"{'Discount (10% over PHP 500):':<32} -PHP {discount:>8.2f}")
        print(f"{'GRAND TOTAL:':<32} PHP {grand_total:>9.2f}")
        print("*"*48)
        print("        Salamat po for your order!        ")
        print("             Have a great day!            \n")


class RestaurantApp:
    def __init__(self):
        self.menu = Menu()
        self.order = Order()

    def run(self):
        self.menu.display()

        while True:
            start_order = input("Would you like to place an order? (y/n): ").strip().lower()
            if start_order in ['y', 'yes']:
                break
            elif start_order in ['n', 'no']:
                print("\nThank you for visiting! Goodbye.")
                sys.exit()
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        self.take_order()
        self.order.print_receipt()

    def take_order(self):
        while True:
            try:
                choice = int(input("Enter the Item ID you wish to order: "))
                menu_item = self.menu.get_item(choice)
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

            self.order.add_item(menu_item, quantity)

            while True:
                again = input("Would you like to order another item? (y/n): ").strip().lower()
                if again in ['y', 'yes', 'n', 'no']:
                    break
                print("Please enter 'y' for yes or 'n' for no.")

            if again in ['n', 'no']:
                break


if __name__ == "__main__":
    app = RestaurantApp()
    app.run()