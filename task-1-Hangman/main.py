import random

words = ["hello","python","hangman","game","world"] # predefined words
word = random.choice(words)

guessed_word = ["_"] * len(word)
attempts = 6

print("WELCOME TO HANGMAN GAME")

while attempts>0 and "_" in guessed_word:
    print("\nWord: "," ".join(guessed_word))  # joining th letters
    guess = input("Enter a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print("Wrong guess! Attempts left: ",attempts)

if "_" not in guessed_word:
    print("\nYou Win! The word was: ",word)
else:
    print("\nYou Loss! The word was: ",word)