def convert_pound(usd):
    """Converts USD to British Pounds."""
    return usd * 0.77

def convert_euro(usd):
    """Converts USD to Euros."""
    return usd * 0.92

def convert_yuan(usd):
    """Converts USD to Chinese Yuan."""
    return usd * 6.98

def main():
    usd = float(input("Enter the dollar amount you wish to convert: "))
    currency_type = input("Enter the desired currency (GBP for Pounds, EUR for Euro, or CNY for Yuan): ").upper()

    if currency_type == "GBP":
        converted_amount = convert_pound(usd)
        print(f"{usd:.2f} USD is equivalent to {converted_amount:.2f} GBP.")
    elif currency_type == "EUR":
        converted_amount = convert_euro(usd)
        print(f"{usd:.2f} USD is equivalent to {converted_amount:.2f} EUR.")
    elif currency_type == "CNY":
        converted_amount = convert_yuan(usd)
        print(f"{usd:.2f} USD is equivalent to {converted_amount:.2f} CNY.")
    else:
        print("Invalid currency code. Please enter GBP, EUR, or CNY.")

if __name__ == "__main__":
    main()
