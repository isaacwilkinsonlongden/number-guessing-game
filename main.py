import random


def main():
    secret_number = random.randint(1, 100)
    print("Welcome to the number guessing game! Please make a guess from 1 - 100.")

    guess = get_valid_guess()  
    attempts = 1

    while guess != secret_number:
        if guess < secret_number:
            print("Too low! Please guess again.")  
        if guess > secret_number:
            print("Too High! Please guess again.")
 
        guess = get_valid_guess() 
        attempts += 1    

    print(f"Congratulations! You guessed correctly!!! It took {attempts} guesses.") 


def get_valid_guess():
    while True:
        try:
            guess = int(input())
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1-100.")
        except ValueError:
            print("Please enter a valid number.")

    
if __name__ == "__main__":
    main()
