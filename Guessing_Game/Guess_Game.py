import random

# Define a function that asks the user for input and DOESN'T QUIT until the user returns something valid
# In this case, "valid" means an integer between 1 and 100 (inclusive)

def get_input():
    while True:
        try:
            guess = input("Guess a number between 1 and 100: ")
            guess = int(guess)
            if guess >= 0 and guess <= 100: 
                return guess
            else: 
                print("Your answer is too big or too small")
        except:
            print("Provide a valid input")


# Define a function that compares the user's input to the answer
# Returns a string that indicates the answer is higher or lower than the input

def compare_input(user, answer):
    if user < answer:
        print("Your input is lower than the correct answer")
    elif user > answer:
        print("Your input is larger than the correct answer")
        second_number = get_input()
        compare_input(second_number, answer)
    elif user == answer:
        print("Correct! ")

    return compare_input



# Define your main() function 

def main():
    # Set a random number between 1 & 100
    answer = random.randint(0,100)
    print(answer)
    player_guess = get_input()
    compare_input(player_guess, answer)


if __name__== "__main__":
    main()
