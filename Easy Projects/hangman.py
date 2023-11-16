import random
from words_list import words

def get_valid_word(words):
    while True: 
        word = random.choice(words)
        if '-' not in word and ' ' not in word:
            return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    used_letters = set()
    word_list = [' ' if letter in word_letters else '_' for letter in word]

    while len(word_letters) > 0:
        print('Selected word:', word)
        print('Word letters:', word_letters)
        print('Used letters:', used_letters)
        print('You have used these letters: ', ' '.join(used_letters))
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        user_letter = user_letter.lower()  # Convert to lowercase
        
        print("You guessed:", user_letter)

        if user_letter.isalpha() and user_letter not in used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)

                for i, letter in enumerate(word):
                    if letter == user_letter:
                        word_list[i] = user_letter

        elif user_letter in used_letters:
            print("You already used that letter")

        else:
            print("Invalid letter")

    print("Congratulations! You've guessed the word:", word)

hangman()



# Instructions
# step 1: select a random word
# step 2: guess a letter
#         if letter is wrong, 1 life is gone 
#         if letter is right, put letter(s) into place
