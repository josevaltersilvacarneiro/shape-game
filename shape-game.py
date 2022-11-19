
def get_secret_word() -> str:

    return 'banana';

def print_header() -> None:

    print('******************************');
    print('* Welcome to the Shape Game! *');
    print('******************************');

def main() -> int:

    secret_word : str = get_secret_word();
    secret_letters_found : list = [ '_' for letter in secret_word ];

    hit : bool = False;
    hung : bool = False;

    while not hit and not hung:

        for letter in secret_letters_found:
            print(letter, end='');
        else:
            print('\nPlaying...');

        guess = input('Type a letter: ').strip().lower();
        index_guess = secret_word.find(guess);

        while index_guess != -1:

            secret_letters_found[index_guess] = guess;
            index_guess = secret_word.find(guess, index_guess + 1);

        if secret_letters_found.count('_') == 0: hit = True;

    print('Game over!');
        
    return 0;

if __name__ == '__main__':
    exit(main())
