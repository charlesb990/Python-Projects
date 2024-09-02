
import random 
def get_user_input():
    while True:
        choice = input("Choose Rock, Paper or Scissors (R,P,S): ").upper()
        if choice in ["ROCK", "R"]:
            return "ROCK"
        elif choice in ["PAPER", "P"]:
            return "PAPER"
        elif choice in ["SCISSORS", "S"]:
            return "SCISSORS"
        else:
            print ("Choice not valid. Try again")
            break
def get_computer_choice():
    computer_choice_num = random.randint(0,2)
    if computer_choice_num == 0:
        return "Rock"
    elif computer_choice_num ==1:
        return "Paper"
    elif computer_choice_num ==2:
        return "Scissors"
def game_result (user_choice, computer_choice):
    if user_choice == computer_choice:
        return "TIE"
    elif user_choice == "ROCK":
        if computer_choice == "SCISSORS":
            return "User wins"
        else:
            return "computer wins"
    elif user_choice == "PAPER":
        if computer_choice == "ROCK":
            return "User wins"
        else:
            return "computer wins"
        
def play_game():
    user_choice = get_user_input()
    if user_choice is None:
        return
    computer_choice = get_computer_choice()
    winner = game_result(user_choice, computer_choice)
    print(f"You selected {user_choice} and the computer selected {computer_choice}")
    if winner == "Tie":
        print("It is a tie")
    else:
        print(f"{winner} wins!")
def main():
    while True:
        play_game()



if __name__ == "__main__":
     main()
