import random

# List of predefined words for the game
WORDS = [
    "python", "hangman", "challenge", "programming",
    "interface", "modular", "optimization", "debugging",
    "development", "testing"
]

# Visual representation of the hangman for each stage
HANGMAN_PICS = [
    """
       -----
       |   |
           |
           |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ---------
    """
]

MAX_ATTEMPTS = len(HANGMAN_PICS) - 1

def get_random_word(word_list):
    """Return a random word from the word list."""
    return random.choice(word_list).lower()

def display_board(hangman_pics, correct_guesses, word, attempts_left):
    """Display the current state of the game."""
    print(hangman_pics[MAX_ATTEMPTS - attempts_left])
    print("Word: " + ' '.join(correct_guesses))
    print(f"Attempts left: {attempts_left}\n")

def get_guess():
    """Prompt the player to enter a guess and return it."""
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        print("Invalid input. Please enter a single letter.")

def play_game():
    """Main function to play the Hangman game."""
    word = get_random_word(WORDS)
    correct_guesses = ['_'] * len(word)
    attempts_left = MAX_ATTEMPTS
    guessed_letters = set()

    print("Welcome to Hangman!")
    
    while attempts_left > 0 and '_' in correct_guesses:
        display_board(HANGMAN_PICS, correct_guesses, word, attempts_left)
        guess = get_guess()

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for idx, letter in enumerate(word):
                if letter == guess:
                    correct_guesses[idx] = guess
        else:
            attempts_left -= 1
            print(f"'{guess}' is not in the word. You lose an attempt.\n")

    display_board(HANGMAN_PICS, correct_guesses, word, attempts_left)

    if '_' not in correct_guesses:
        print(f"Congratulations! You've guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    play_game()
