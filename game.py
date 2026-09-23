import random
import os

SCORE_FILE = "highscore.txt"

def get_high_score():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            try:
                return int(f.read().strip())
            except ValueError:
                return None
    return None

def save_high_score(score):
    with open(SCORE_FILE, "w") as f:
        f.write(str(score))

def play_game():
    secret_number = random.randint(1, 50)
    attempts = 0
    high_score = get_high_score()
    
    print("\n==================================")
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 50.")
    if high_score:
        print(f"🏆 Current All-Time High Score: {high_score} guesses")
    else:
        print("🏆 No high score set yet. Be the first!")
    print("==================================")
    
    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > 50:
                print("Please guess a number between 1 and 50!")
                continue
                
            if guess < secret_number:
                print("Too low! 📉 Try a higher number.")
            elif guess > secret_number:
                print("Too high! 📈 Try a lower number.")
            else:
                print(f"\n🎉 CONGRATULATIONS! You got it in {attempts} attempts!")
                
                if high_score is None or attempts < high_score:
                    print(" New All-Time Record Set! 🏆")
                    save_high_score(attempts)
                break
        except ValueError:
            print("Oops! That's not a valid number. Try again.")

play_game()

