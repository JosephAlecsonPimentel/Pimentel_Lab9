def display_menu():
    """"""
    """Displays the food menu with prices."""
    menu = {
        "Adobo": 70.00,
        "Sisig": 89.00,
        "Menudo": 75.00,
        "lechon Kawali": 80.00,
        "Bagnet": 80.00,
        "Tapsilog": 100.00,
        "Chicken Inasal": 120.00,
        "Dinuguan": 85.00  
    }
    
    print("Welcome to Karenderya Food Ordering System")
    print("Please choose an list from the food menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")
    
    return menu

def take_order(menu):
    """ # Allow the user to choose an item from the menu.."""
    while True:
        choice = input("Enter the food item you'd like to order: ").strip().capitalize()
        if choice in menu:
            print(f"You have selected {choice} which costs ₱{menu[choice]:.2f}.")
            return choice, menu[choice]
        else:
            print("Invalid selection. Please choose a valid item from the menu. ")

def process_payment(total):
    """ # Handles payment process, ensures the cash given is sufficient, and give it back to the change."""
    while True:
        try:
            cash = float(input(f"Total is ₱{total:.2f}. Please enter the amount of cash you are paying: ₱"))
            if cash < total:
                print(f"Insufficient funds. You need ₱{total - cash:.2f} more.")
            else:
                change = cash - total
                print(f"Payment successfully Your change is: ₱{change:.2f}")
                print("Thank You come back again ")
                return change
        except ValueError:
            print("Invalid input. Please enter a exact amount.")

def main():
    """Main function to run the food ordering system."""
    menu = display_menu()
    item, price = take_order(menu)
    total = price
    process_payment(total)

if __name__ == "__main__":
    main()
input