import os
from random import randint

def push_secret_word(word : str) -> None:

    with open('secret-words.txt', 'a') as fil:
        fil.write(word + '\n');

def get_secret_word() -> str:

    with open('secret-words.txt', 'r') as fil:
        words = fil.read().split('\n');

    line = randint(0, len(words) - 1);
    return words[line];

def update(secret_letters_found : list) -> None:

    os.system('clear');                      # It cleans the console

    print('******************************');
    print('* Welcome to the Shape Game! *');
    print('******************************');

    for letter in secret_letters_found:
        print(letter, end='');
    else:
        print();

def main() -> int:

    secret_word : str = get_secret_word();
    secret_letters_found : list = [ '_' for letter in secret_word ];

    hit : bool = False;
    hung : bool = False;

    while not hit and not hung:

        update(secret_letters_found);        # Update the screen

        while (guess := input('Type a letter: ').strip().lower()) in secret_letters_found: pass
        index_guess = secret_word.find(guess);

        while index_guess != -1:

            secret_letters_found[index_guess] = guess;
            index_guess = secret_word.find(guess, index_guess + 1);

        if secret_letters_found.count('_') == 0: hit = True;

    else:

        update(secret_letters_found);        # Update the screen
        print('Game over!');

        new_secret_word = input('Type a new secret word: ');
        push_secret_word(new_secret_word);
        
    return 0;

if __name__ == '__main__':
    exit(main())
