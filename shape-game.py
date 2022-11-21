import os

def get_secret_word() -> str:

    return 'banana';

def update(secret_letters_found : list) -> None:

    os.system('clear');                      # It clean the console

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
        
    return 0;

if __name__ == '__main__':
    exit(main())
