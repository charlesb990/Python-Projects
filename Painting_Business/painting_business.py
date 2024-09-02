import math

def calculate_paint(square_feet):
   gallons_per_square_foot = 1/115
   gallons_needed = square_feet * gallons_per_square_foot
   return gallons_needed

def calculate_labor(square_feet):
   hours_per_squarefoot = 8/115
   hours_needed = square_feet * hours_per_squarefoot
   return hours_needed 

def main ():
   square_feet = float(input("Enter the number of square feet that needs painted: "))
   paint_price = float(input("Enter the price of the paint selected: "))
   gallons_required = calculate_paint(square_feet)
   labor_hours = calculate_labor(square_feet)
   labor_cost = labor_hours * 20
   paint_cost = gallons_required * paint_price
   total_cost = paint_cost + labor_cost

   print(f"Paint required: {gallons_required:.2f} gallons ")
   print(f"The hours of labor required: {labor_hours:.2f}h")
   print(f"Cost of paint: ${paint_cost:.2f}")
   print(f"Labor charges ${labor_cost:.2f}")
   print(f"The total is: ${total_cost:.2f}")
if __name__ == "__main__":
   main()
