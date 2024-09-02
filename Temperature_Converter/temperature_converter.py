def celsius_to_fahrenheit():
    celsius = float(input("Enter the temperature in celsius: "))
    return celsius

def conversion(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def main():
    celsius = celsius_to_fahrenheit()
    fahrenheit = conversion(celsius)

    print (f"The temperature in fahrenheit is: {fahrenheit:.2f} ")
    print(f"The temperature in celsius is: {celsius:.f}")

if __name__ == "__main__":
    main()
