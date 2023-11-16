import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "algorithm", "javascript"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print(f"Word: {display_word(word_to_guess, guessed_letters)}")
        print(f"Attempts left: {attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word_to_guess:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            attempts -= 1
        
        if set(word_to_guess) == set(guessed_letters):
            print(f"Congratulations! You won! The word was '{word_to_guess}'.")
            break

    if attempts == 0:
        print(f"Sorry, you ran out of attempts. The word was '{word_to_guess}'.")

if __name__ == "__main__":
    hangman()
