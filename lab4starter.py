# No Imports are required for this program

def main():
    
    # Hardcoded orders
    # A Dictionary is used to store the orders
    # Key: Order number
    # Value: List of menu items
    orders = {
        1: ['burger', 'fries', 'soda', 'apple pie'],
        2: ['pizza', 'salad', 'breadsticks', 'water'],
        3: ['pasta', 'garlic bread', 'wine', 'cheesecake'],
        4: ['steak', 'mashed potatoes', 'green beans', 'ice cream'],
        5: ['chicken sandwich', 'coleslaw', 'lemonade', 'brownie']
    }

    # Hardcoded menu
    # A Dictionary is used to store the menu items and their prices
    # Key: Menu item
    # Value: Price
    menu = {
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
        'wine': 9.99,
        'cheesecake': 4.99,
        'steak': 14.99,
        'mashed potatoes': 3.99,
        'green beans': 2.99,
        'ice cream': 3.99,
        'chicken sandwich': 6.99,
        'coleslaw': 1.99,
        'lemonade': 2.50,
        'brownie': 2.99
    }

    # Display open orders
    # Print statements are used to display the output
    print("Orders:")
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")

    # Read order number from input
    order_number = int(input("Which order would you like to generate a receipt for? "))

    # Get the order
    # .get method is used to get the value from the dictionary
    order = orders.get(order_number, [])

    # Receipt Generation
    # .get method is used to get the value from the dictionary
    total = sum(map(menu.get, order))
    
    # Print the receipt
    # f strings are used to format the output
    print("\nReceipt:")
    print(f"{order[0]}: ${menu[order[0]]:.2f}")
    print(f"{order[1]}: ${menu[order[1]]:.2f}")
    print(f"{order[2]}: ${menu[order[2]]:.2f}")
    print(f"{order[3]}: ${menu[order[3]]:.2f}")
    
    tax = total * 0.05
    
    print(f"Total: ${total:.2f}")
    print(f"Tax (5%): ${tax:.2f}")

    # Tip Options
    tip_percentages = {"a": 0.15, "b": 0.20, "c": 0.25}
    print("\nTip options:")
    
    # Calculate and print the tip options
    # f strings are used to format the output
    tip_option_a = f"a) 15%: ${total * 0.15:.2f} (Total: ${(total + total * 0.15 + tax):.2f})"
    tip_option_b = f"b) 20%: ${total * 0.20:.2f} (Total: ${(total + total * 0.20 + tax):.2f})"
    tip_option_c = f"c) 25%: ${total * 0.25:.2f} (Total: ${(total + total * 0.25 + tax):.2f})"
    
    # Print the tip options
    print(tip_option_a)
    print(tip_option_b)
    print(tip_option_c)

    # Final Payment
    # Read tip choice from input
    tip_choice = input("Choose a tip option (a, b, c): ")
    tip_percentage = tip_percentages.get(tip_choice, 0)
    print(f"Selected tip percentage: {int(tip_percentage*100)}%")

    # Calculate and print the total bill
    # Total bill = Total + Tax + Tip
    # Thank you message
    total_bill = total + tax + (total * tip_percentage)
    print(f"Total bill: ${total_bill:.2f}")
    print("Thank you for dining with Python Gourmet!")

if __name__ == "__main__":
    main()