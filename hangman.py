"""
file: hangman.py
language: python 3
author: Aakash Jaideva
purpose: A simple game of Blackjack
"""

import random


def display_word(word, guessed_letters):
    """
    Generate a display string for the word, revealing guessed letters and hiding others.

    Parameters:
    - word (str): The target word to be guessed.
    - guessed_letters (set): Set of letters that the player has guessed.

    Returns:
    - str: Display string with guessed letters revealed and others hidden.
    """
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()


def main():
    """
    Main function to run the Hangman game.
    """
    print("Welcome to Hangman")

    # List of words that can be chosen for the game
    word_list = ['ardvark', 'baboon', 'camel', 'Elephant', 'Computer', 'Universe', 'Sunshine', 'Butterfly', 'Chocolate',
                 'Adventure', 'Happiness', 'Mountain', 'Watermelon']

    # Randomly select a word from the list
    word_choice = random.choice(word_list)

    # Set to store guessed letters
    guessed_letters = set()

    # Counter for total attempts allowed
    total_attempts = 0

    # Main game loop
    while total_attempts < 7:
        # Display the current state of the word
        current_display = display_word(word_choice, guessed_letters)
        print(f"\n{current_display}")

        # Check if all letters have been guessed
        if set(word_choice) == guessed_letters:
            print("Congratulations! You guessed the word:", word_choice)
            break

        # Get user input for a letter
        answer_input = input('\nEnter a letter: ').lower()

        # Validate user input
        if answer_input.isalpha() and len(answer_input) == 1:
            if answer_input in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif answer_input in word_choice:
                guessed_letters.add(answer_input)
                print("Right!")
            else:
                total_attempts += 1
                print("Wrong! Attempts remaining:", 7 - total_attempts)
        else:
            print("Please enter a valid single letter.")

    # Check if the player ran out of attempts
    if total_attempts == 7:
        print("Sorry, you ran out of attempts. The word was:", word_choice)


if __name__ == '__main__':
    # Run the Hangman game
    main()
