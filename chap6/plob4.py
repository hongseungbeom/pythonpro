import random as rd
word_list = ["python", "hangman", "programming", "catholic"]

def play_hangman():
    word_to_guess = rd.choice(word_list)
    guessed_word = ["-"] * len(word_to_guess)
    max_attempts = 5
    incorrect_attempts = 0
    guessed_letters = []

    while True:
        print_hangman(incorrect_attempts)
        print("You've used the following letters:", guessed_letters)
        print("So far the word is")
        print("\n" + "".join(guessed_word))
        if "".join(guessed_word) == word_to_guess:
            print("Congratulations! You guessed the word:", word_to_guess)
            break

        if incorrect_attempts >= max_attempts:
            print("You failed to guess the word. The word was:", word_to_guess)
            break

        guess = input("Enter your guess: ").lower()
        guessed_letters.append(guess)

        if guess in word_to_guess:
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    guessed_word[i] = guess
        else:
            incorrect_attempts += 1

def print_hangman(incorrect_attempts):
    hangman_parts = [
        ["-----|-"],
        ["|    0"],
        ["|   -+- "],
        ["|    |"],
        ["|   /|"],
        ]

    for i in range(incorrect_attempts):
        print("\n".join(hangman_parts[i]))

if __name__ == "__main__":
    play_hangman()
