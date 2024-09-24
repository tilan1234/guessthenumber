import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number within the range of 1 to 100.")
            elif guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

    if attempts == max_attempts:
        print(f"Sorry! You have used all your attempts. The number was {number_to_guess}.")

# Run the game
guess_the_number()
