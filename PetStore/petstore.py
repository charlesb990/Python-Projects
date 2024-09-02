item_details = []
item_details.append({"type": "bird food", "price": 5.99})
item_details.append({"type": "leash", "price": 15.00})
item_details.append({"type": "collar", "price": 9.99})
item_details.append({"type": "dog food", "price": 20.99})
item_details.append({"type": "cat food", "price": 18.99})

tax_rate = 0.07 

def item_price(item):
    for item_info in item_details:
        if item_info ["type"] == item:
            return item_info ["price"]
    return None
def get_quantity(item_type):
    while True:
        try:
            quantity = int(input(f"Enter quantity of {item_type}: "))
            if quantity > 0:
                return quantity
            else:
                print("Quantity must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
def calculate_subtotal(item_price, quantity):
    return item_price * quantity
def calculate_tax (subtotal, tax_rate):
    return subtotal * tax_rate
def calculate_total(subtotal, tax):
    return subtotal + tax

def print_purchase_details (purchase_items):
    print("\n--- Purchase Summary ---")
    for item in purchase_items:
        print(f"{item['type']} x {item['quantity']} - ${item['subtotal']:.2f}")
    total_cost = sum(item['subtotal'] for item in purchase_items)
    total_tax = calculate_tax(total_cost, tax_rate)
    grand_total = calculate_total(total_cost, total_tax)
    print(f"Subtotal: ${total_cost:.2f}")
    print(f"Tax: ${total_tax:.2f}")
    print(f"Grand Total: ${grand_total:.2f}")
          
def main():
    print("Welcome to the Pet Store!")
    purchase_items = []

    while True:
        item_type = input("Enter item type (or 'q' to quit): ")
        if item_type == "q":
            break

        quantity = get_quantity(item_type)
        item_price_info = item_price(item_type)

        if item_price_info is None:
            print("Item not found. Please try again.")
            continue

        subtotal = calculate_subtotal(item_price_info, quantity)
        purchase_items.append({"type": item_type, "quantity": quantity, "subtotal": subtotal})

    # Print purchase details and final cost
    print_purchase_details(purchase_items)


   

if __name__ == "__main__":
    main()
