def calculate_fee (membership, time_biking):

    if membership == "D":
        total_ride = (time_biking * 0.20) + 1.50
    else:
        total_ride = (time_biking * 0.15) + 1.00

    return total_ride

def taxing (total_ride):
    tax = total_ride * 0.08
    return tax

def main():
    membership = input("Select the type of membership D or A: ")
    time_biking = input("Input the time in minutes that you used the bike: ")
    time_biking = float(time_biking)
    total_rid = calculate_fee (membership, time_biking)
    total_tax = taxing(total_rid)
    total_pay = total_rid + total_tax
    total_rid = print(f"Your total cost is ${total_rid:.2f} your tax is ${total_tax:.2f} and your total is ${total_pay:.2f} ")





if __name__ == "__main__":
    main()
