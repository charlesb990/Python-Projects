print("Welcome to the Fast Freight Shipping Company".title().upper())

def shipping_cost(weight):
    if weight <= 2:
        price = weight * 1.10
    if 2 < weight <= 6:
        price = weight * 2.20
    if 6 < weight <= 10:
        price = weight * 3.70
    if weight >10:
        price = weight * 3.80
    return price 

def subtotal(shipping_cost):

    return shipping_cost * 0.08

def tax (subtotal):
    return subtotal * 0.08
    

def main():
    weight = float((input("Input the weight: ")))
    cost = shipping_cost(weight)
    taxes = tax(cost)
    total_cost = cost + taxes
    print(f"The cost is USD {cost:.2f}")
    print(f"Your tax is USD {taxes:.2f}")
    print(f"Your total is {total_cost:.2f}")    

if __name__ == "__main__":
    main()
