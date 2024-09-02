import csv

def getCustomer(phone_num):
    file = 'code/dd_customer_list.csv'
    with open(file) as csvfile:
        customers = csv.DictReader(csvfile, delimeter=",")
        for customer in customers:
            if customer["phone_number"] == phone_num:
                return customer
        
        customer_first_name = input("Enter the customer's first name: ")
        customer_last_name = input("Enter the customer's last name: ")
        customer_phone_number = input("Enter the customer's phone number:")
        newcustomer = {}
        newcustomer["first_name"] = customer_first_name
        newcustomer["last_name"] = customer_last_name
        newcustomer["phone_number"] = customer_phone_number
        return newcustomer
    
def order_capture():
    while True:
        try:
            cake_num = int(input("Enter the number of cupcakes sold: "))
            if cake_num > 0:
                return cake_num
            else:
                print("Please enter a positive number. ")
        except:
            print("Your input is not a number, try again.")

def cal_subtotal(cake_num):
    if cake_num >=5:
        return 4.00 *cake_num
    else:
        return 5.00 * cake_num 


def cal_tax(subtotal_amount):
    return subtotal_amount * 0.08



def cal_total (subtotal_amount, tax_amount):
    return subtotal_amount + tax_amount


def display_info(customer, cake_num, subtotal_amount, tax_amount, total_amount):
    print(f"your order for: ")
    print(f"first name: {customer['first_name']}")
    print(f"Last name: {customer['last_name']}")
    print(f"phone: {customer['phone_number']}")
    print(f"you ordered {cake_num}.")
    print(f"your subtotal is ${subtotal_amount}.")
    print(f"tax is ${tax_amount}")
    print(f"total amount due is 4{total_amount}")


def main():
    print("Welcome to Donna's Delights")
    phone_num = input("Enter the phone number of the customer:")
    customer = GetCustomer(phone_num)
    cake_num = order_capture()
    subtotal_amount = cal_subtotal(cake_num)
    tax_amount = cal_tax(subtotal_amount)
    total_amount = cal_total(subtotal_amount, tax_amount)
    display_info(customer, cake_num, subtotal_amount, tax_amount, total_amount)

if __name__== "__main__":
    main()
