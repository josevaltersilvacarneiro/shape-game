import os
from random import choice 
from termcolor import colored

def push_secret_word(word : str) -> None:

    with open('secret-words.txt', 'a') as fil:
        fil.write(word + '\n');

def get_secret_word() -> str:

    with open('secret-words.txt', 'r') as fil:
        words = fil.readlines();

    word = choice(words);
    return word.strip();

def get_the_guess(secret_letters_found : list) -> str:

    while (guess := input('Type a letter: ').strip().lower()) in secret_letters_found:
        pass

    return guess;

def update(secret_letters_found : list) -> None:

    os.system('clear');                      # It cleans the console

    print('******************************');
    print('* Welcome to the Shape Game! *');
    print('******************************');

    for letter in secret_letters_found:
        letter = colored(letter, 'red');     # It colors the output
        print(letter, end='');
    else:
        print();

def main() -> int:

    secret_word : str = get_secret_word();
    secret_letters_found : list = [ '_' for letter in secret_word ];

    hit : bool = False;
    hung : bool = False;

    while not hit and not hung:

        update(secret_letters_found);                # Update the screen
        guess = get_the_guess(secret_letters_found);

        index_guess = secret_word.find(guess);
        while index_guess != -1:

            secret_letters_found[index_guess] = guess;
            index_guess = secret_word.find(guess, index_guess + 1);

        hit = '_' not in secret_letters_found;

    else:

        update(secret_word);                         # Update the screen
        print('Game over!');

        new_secret_word = input('Type a new secret word: ');
        push_secret_word(new_secret_word);
        
    return 0;

if __name__ == '__main__':
    exit(main())
