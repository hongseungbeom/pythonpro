import random as rd

words = ['difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university']

print("Guess the Word!!!")
print("In this game, the program selects a word at random, and the player's objective is to guess the chosen word.\n\n")

word = rd.choice(words)
print("Length of the selected word:", len(word))

guesswd = ''
chance = 6

guessed_word = ['_' for _ in word]

while chance > 0:

    for i in range(len(word)):
        if word[i] in guesswd:
            guessed_word[i] = word[i]

    print("Remaining attempts:", chance)
    print("Current guessed word:", end=' ')
    for letter in guessed_word:
        print(letter, end=' ')
    print()

    if ''.join(guessed_word) == word:
        print("Congratulations! You guessed the word:", word)
        chance= 0
        break

    guesssp = input("\nGuess a letter:")
    guesswd += guesssp

    if guesssp not in word:
        chance -= 1
        print("Incorrect guess")

        if chance == 0:
            print("You've used up all your attempts. The correct word was", word)
            break
