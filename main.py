import random


def main():
    secret_number = random.randint(1, 100)
    guess = None
    print("Welcome to the number guessing game! Please make a guess from 1 - 100.")

    while type(guess) != int:
        try:
            guess = int(input())
        except ValueError:
            print("Please enter a valid number.")  

    attempts = 1

    while guess != secret_number:
        if guess < secret_number:
            print("Too low! Please guess again.")  
        if guess > secret_number:
            print("Too High! Please guess again.")

        guess = None
 
        while type(guess) != int:
            try:
                guess = int(input())
            except ValueError:
                print("Please enter a valid number.") 

        attempts += 1    

    print(f"Congratulations! You guessed correctly!!! It took {attempts} guesses") 
    
    
if __name__ == "__main__":
    main()
