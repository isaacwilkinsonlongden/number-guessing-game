import random
import sys


def play_game():
    while True:
        main()
        play_again = input("Play again? y/n: ").strip().lower()
        if play_again not in ("y", "yes"):
            print("Thanks for playing!")
            break


def main():
    secret_number = random.randint(1, 100)
    print("----------------------------------------------------------------------")
    print("Welcome to the number guessing game! Please make a guess from 1 - 100.")
    print("----------------------------------------------------------------------")

    guess = get_valid_guess()  
    attempts = 1

    while guess != secret_number:
        if guess < secret_number:
            print("Too low! Please guess again.")  
        elif guess > secret_number:
            print("Too high! Please guess again.")
 
        guess = get_valid_guess() 
        attempts += 1    

    print("----------------------------------------------------------------------")
    print(f"Congratulations! You guessed correctly!!! It took {attempts} guesses.")
    print("----------------------------------------------------------------------") 


def get_valid_guess():
    while True:
        try:
            guess = int(input("Enter your guess or type '0' to quit: "))
            if 1 <= guess <= 100:
                return guess
            elif guess == 0:
                exit_program()    
            else:
                print("Please enter a number between 1-100.")
        except ValueError:
            print("Please enter a valid number.")


def exit_program():
    print("-----------------------")
    print("Ok quitting the game :(")
    print("-----------------------")
    sys.exit()

    
if __name__ == "__main__":
    play_game()
