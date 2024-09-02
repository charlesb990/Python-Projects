import random

def guess_number():
    number_to_guess = random.randint(1,100)
    used_numbers = []
    while True:
        try:
            user_number = int(input("Enter a number between 1 and 100: "))
            used_numbers.append(user_number)
            if user_number > number_to_guess:
                print("Your bet is too high! try again, friend")
            elif user_number < number_to_guess:
                print("That is too small. Try again!")
            else:
                print(f"congrats that is the right number!!! {', '.join(str(num) for num in used_numbers[:-1])} and {used_numbers[-1]} (total: {len(used_numbers)}) guesses.")
                break
        except ValueError:
            print("That is not a number. Try a number from 1 to 100")
            return guess_number

def main():
    print("Welcome to the guessing game!")
    guess_number()

if __name__ == "__main__":
    main()
