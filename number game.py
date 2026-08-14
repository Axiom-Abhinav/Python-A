import random
import sys

def guess_the_number_game():
    """A classic 'Guess the Number' game."""
    
    print("-------------------------------------------------")
    print("       Welcome to Guess the Number! 🧠          ")
    print("-------------------------------------------------")
    
    # 1. Game Setup
    # Generate a random number between 1 and 100
    LOWER_BOUND = 1
    UPPER_BOUND = 1000
    SECRET_NUMBER = random.randint(LOWER_BOUND, UPPER_BOUND)
    MAX_ATTEMPTS = 15
    attempts_left = MAX_ATTEMPTS
    
    print(f"\nI'm thinking of a number between {LOWER_BOUND} and {UPPER_BOUND}.")
    print(f"You have {MAX_ATTEMPTS} attempts to guess it.")
    
    # 2. Main Game Loop
    while attempts_left > 0:
        print(f"\n--- Attempts left: {attempts_left} ---")
        
        try:
            # Get user input
            guess_str = input("Take a guess (enter a number): ")
            guess = int(guess_str)
            
            # Check if the guess is within the valid range
            if not (LOWER_BOUND <= guess <= UPPER_BOUND):
                print(f"⚠️ Your guess must be between {LOWER_BOUND} and {UPPER_BOUND}. Try again.")
                # Do not decrement attempts for range errors
                continue 
            
        except ValueError:
            # Handle non-integer input
            print("❌ Invalid input! Please enter a whole number.")
            # Do not decrement attempts for type errors
            continue 

        # 3. Check the Guess
        if guess < SECRET_NUMBER:
            print("⬆️ Too low! Guess higher.")
        elif guess > SECRET_NUMBER:
            print("⬇️ Too high! Guess lower.")
        else:
            # Player wins
            attempts_used = MAX_ATTEMPTS - attempts_left + 1
            print("\n=============================================")
            print(f"🎉 CONGRATULATIONS! You guessed the number {SECRET_NUMBER}!")
            print(f"It took you {attempts_used} attempt(s) and {attempts_left} attempts remaining.")
            print("You are a true number wizard! 🧙‍♂️")
            print("=============================================")
            return # Exit the function/game

        attempts_left -= 1 # Decrement attempts after a valid guess

    # 4. Player Loses (After loop finishes)
    print("\n=============================================")
    print("😭 GAME OVER! You ran out of attempts.")
    print(f"The secret number was {SECRET_NUMBER}.")
    print("=============================================")

if __name__ == "__main__":
    try:
        guess_the_number_game()
    except KeyboardInterrupt:
        print("\n\nGame closed. Goodbye!")
        sys.exit(0)