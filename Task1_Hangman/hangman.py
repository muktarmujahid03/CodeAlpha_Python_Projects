import random

WORDS = ["python", "computer", "security", "network", "program"]

def display_word(secret_word, guessed_letters):
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )

def play_game():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("\n=== HANGMAN GAME ===")
    print("Guess the hidden word one letter at a time.")
    print(f"You can make {max_wrong_guesses} incorrect guesses.")

    while wrong_guesses < max_wrong_guesses:
        print("\nWord:", display_word(secret_word, guessed_letters))
        print("Incorrect guesses:", wrong_guesses, "/", max_wrong_guesses)

        guess = input("Enter one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct!")
            if all(letter in guessed_letters for letter in secret_word):
                print("\nCongratulations! You guessed:", secret_word)
                return
        else:
            wrong_guesses += 1
            print("Sorry, that letter is not in the word.")

    print("\nGame over! The word was:", secret_word)

if __name__ == "__main__":
    play_game()
