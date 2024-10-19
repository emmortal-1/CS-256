# No Imports are required for this program
def main():
    """
    Main function to run the Restaurant Receipt Generator.
    """
    orders = get_orders()
    menu = get_menu()
    display_open_orders(orders)
    order_number = get_order_number()
    order = orders.get(order_number, [])
    total, tax = generate_receipt(order, menu)
    tip_percentage = display_tip_options(total, tax)
    calculate_total_bill(total, tax, tip_percentage)

def get_orders():
    """
    Returns a dictionary of hardcoded orders.
    Key: Order number
    Value: List of menu items
    """
    return {
        1: ['burger', 'fries', 'soda', 'apple pie'],
        2: ['pizza', 'salad', 'breadsticks', 'water'],
        3: ['pasta', 'garlic bread', 'wine', 'cheesecake'],
        4: ['steak', 'mashed potatoes', 'green beans', 'ice cream'],
        5: ['chicken sandwich', 'coleslaw', 'lemonade', 'brownie']
    }

def get_menu():
    """
    Returns a dictionary of hardcoded menu items and their prices.
    Key: Menu item
    Value: Price
    """
    return {
        'burger': 5.99,
        'fries': 2.99,
        'soda': 1.50,
        'apple pie': 3.99,
        'pizza': 8.99,
        'salad': 4.99,
        'breadsticks': 3.99,
        'water': 0.00,
        'pasta': 7.99,
        'garlic bread': 2.99,
        'wine': 6.99,
        'cheesecake': 4.99,
        'steak': 14.99,
        'mashed potatoes': 3.99,
        'green beans': 2.99,
        'ice cream': 3.50,
        'chicken sandwich': 6.99,
        'coleslaw': 2.50,
        'lemonade': 1.99,
        'brownie': 2.99
    }

def display_open_orders(orders):
    """
    Displays the list of open orders.
    """
    print("Open Orders:")
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")

def get_order_number():
    """
    Prompts the user to enter an order number and returns it.
    """
    return int(input("Which order would you like to generate a receipt for? "))

def generate_receipt(order, menu):
    """
    Generates and prints the receipt for the given order.
    """
    total = sum(map(menu.get, order))
    print("\nReceipt:")
    if len(order) > 0:
        print(f"{order[0]}: ${menu[order[0]]:.2f}")
    if len(order) > 1:
        print(f"{order[1]}: ${menu[order[1]]:.2f}")
    if len(order) > 2:
        print(f"{order[2]}: ${menu[order[2]]:.2f}")
    if len(order) > 3:
        print(f"{order[3]}: ${menu[order[3]]:.2f}")
    tax = total * 0.05
    print(f"Total: ${total:.2f}")
    print(f"Tax (5%): ${tax:.2f}")
    return total, tax

def display_tip_options(total, tax):
    """
    Displays the tip options and returns the selected tip percentage.
    """
    tip_percentages = {"a": 0.15, "b": 0.20, "c": 0.25}
    print("\nTip options:")
    
    # Manually print each tip option
    tip_amount_a = total * tip_percentages["a"]
    final_total_a = total + tax + tip_amount_a
    print(f"a) 15%: ${tip_amount_a:.2f} (Total: ${final_total_a:.2f})")
    
    tip_amount_b = total * tip_percentages["b"]
    final_total_b = total + tax + tip_amount_b
    print(f"b) 20%: ${tip_amount_b:.2f} (Total: ${final_total_b:.2f})")
    
    tip_amount_c = total * tip_percentages["c"]
    final_total_c = total + tax + tip_amount_c
    print(f"c) 25%: ${tip_amount_c:.2f} (Total: ${final_total_c:.2f})")
    
    tip_choice = input("Choose a tip option (a, b, c): ")
    return tip_percentages.get(tip_choice, 0)

def calculate_total_bill(total, tax, tip_percentage):
    """
    Calculates and prints the total bill amount.
    """
    total_bill = total + tax + (total * tip_percentage)
    print(f"Selected tip percentage: {int(tip_percentage*100)}%")
    print(f"Total bill: ${total_bill:.2f}")
    print("Thank you for dining with Python Gourmet!")

if __name__ == "__main__":
    main()