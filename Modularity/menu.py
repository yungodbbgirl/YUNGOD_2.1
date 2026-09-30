def display_menu(menu_dict):
    print("\n" + "="*45)
    print("        WELCOME TO BB.GIRL'S RESTAURANT      ")
    print("="*45)
    print(f"{'ID':<5} {'Item':<22} {'Price':>15}")
    print("-" * 45)
    for item_id, details in menu_dict.items():
        print(f"{item_id:<5} {details['name']:<22} PHP {details['price']:>9.2f}")
    print("="*45 + "\n")