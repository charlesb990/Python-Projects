import random

# Function to generate a random fruit
def generate_fruit(min_value, max_value):
  fruit_map = {1: "Cherries", 2: "Oranges", 3: "Plums"}
  random_number = random.randint(min_value, max_value)
  return fruit_map[random_number]

# Main program loop
while True:
  # Get user input for money
  while True:
    try:
      money = float(input("Enter the amount of money you want to insert: $ "))
      if money <= 0:
        print("Invalid amount. Please enter a positive value.")
      else:
        break
    except ValueError:
      print("Invalid input. Please enter a number.")

  # Spin the reels
  reel1 = generate_fruit(1, 3)
  reel2 = generate_fruit(1, 3)
  reel3 = generate_fruit(1, 3)

  # Display the results
  print("You spin:", reel1, ",", reel2, ",", reel3)

  # Calculate winnings
  win_amount = 0
  if reel1 == reel2 and reel2 == reel3:
    win_amount = money * 3  # Triple winnings for all match
  elif reel1 == reel2 or reel1 == reel3 or reel2 == reel3:
    win_amount = money * 2  # Double winnings for two matches

  # Display winnings
  if win_amount > 0:
    print("Congratulations! You win $", win_amount)
  else:
    print("Sorry, no match. You win $0")

  # Ask to play again
  play_again = input("Do you want to play again (y/n)? ").upper()
  if play_again != "Y":
    break

print("Thank you for playing!")
