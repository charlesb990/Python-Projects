
def main():
    while True:
        try:
            hourly_rate = validate_rate()
            hours_worked = validate_info()
            gross_pay = hourly_rate * hours_worked
            print(f"The gross pay is ${gross_pay:.2f}")
            break
        except ValueError as b:
            print(f"Error {b}")


def validate_rate():
    while True:
        try:
            hour_rate =  float(input("Enter the hourly rate of the salary between $7.50 and $18.25: "))
            if 7.50 <= hour_rate<= 18.25:
                return hour_rate
            else:
                print("Invalid number. try again")
        except:
            print("Not a valid input. try again") 


def validate_info():
    while True:
        try:
            hours_worked = int(input("enter the number of hours worked (0-40): "))
            if 0<= hours_worked <= 40:
                return hours_worked
            else:
                print("Try again")
        except:
            print("Introduce a number between 0 and 40")
    

        
if __name__ == "__main__":
  main()
