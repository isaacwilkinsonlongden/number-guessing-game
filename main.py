import random
import sys
import os


def play_game():
    while True:
        main()
        play_again = input("Play again? y/n: ").strip().lower()
        if play_again not in ("y", "yes"):
            print("-------------------")
            print("Thanks for playing!")
            print("-------------------")
            break


def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    low, high, max_guesses = difficulty()
    secret_number = random.randint(low, high)
    print("----------------------------------------------------------------------")
    print(f"Welcome to the number guessing game! Please make a guess from {low} - {high}.")
    print("----------------------------------------------------------------------")

    guess = get_valid_guess(low, high)  
    attempts = 1

    while guess != secret_number:
        if attempts == (max_guesses - 3):
            print("You have 3 guesses left!")
        elif attempts == (max_guesses - 1):
            print("LAST CHANCE!")    
        elif attempts == max_guesses:
            print("----------------------------------")
            print("GAME OVER! YOU RAN OUT OF GUESSES.")
            print(f"The secret number was {secret_number}")
            print("----------------------------------")
            return

        if guess < secret_number:
            print("Too low! Please guess again.")
            print("----------------------------")  
        elif guess > secret_number:
            print("Too high! Please guess again.")
            print("-----------------------------")

        guess = get_valid_guess(low, high) 
        attempts += 1    

    print("----------------------------------------------------------------------")
    print(f"Congratulations! You guessed correctly!!! It took {attempts} guesses.")
    print("----------------------------------------------------------------------") 


def get_valid_guess(low, high):
    while True:
        try:
            guess = int(input("Enter your guess or type '0' to quit: "))
            if low <= guess <= high:
                return guess
            elif guess == 0:
                exit_program()    
            else:
                print(f"Please enter a number between {low}-{high}.")
                print("------------------------------------")
        except ValueError:
            print("Please enter a valid number.")
            print("----------------------------")


def difficulty():
    while True:
        print("Please choose a difficulty:")
        print("Easy:   1-10")
        print("Medium: 1-100")
        print("Hard:   1-200")
        print("Elite:  1-1000")
        difficulty = input("Your choice (easy, medium, hard, elite): ").strip().lower()

        if difficulty == "easy":
            return 1, 10, 4
        elif difficulty == "medium":
            return 1, 100, 7
        elif difficulty == "hard":
            return 1, 200, 8
        elif difficulty == "elite":
            return 1, 1000, 9
        else:
            print("Please enter a valid difficulty")
            print("-------------------------------")    


def exit_program():
    print("-----------------------")
    print("Ok quitting the game :(")
    print("-----------------------")
    sys.exit()

    
if __name__ == "__main__":
    play_game()
