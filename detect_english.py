UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def load_dictionary():
    with open('dictionary.txt') as f:
        english_words = {word for word in f.read().split('\n')}
    
    return english_words

ENGLISH_WORDS = load_dictionary()

def get_english_count(message):
    message = message.upper()
    message = remove_non_letters(message)
    possible_words = message.split()

    num_words = len(possible_words)

    if num_words == 0:
        return 0.0
    
    matches = 0
    for word in possible_words:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / num_words


def remove_non_letters(message):
    letters = [symbol for symbol in message if symbol in LETTERS_AND_SPACE]
    return ''.join(letters)


def is_english(message, word_percentage = 20, letter_percentage = 85):
    '''
    By default, 20% of th ewords must exist in the dictionary file, and
    85% of all the characters in the message must be letters or spaces.
    '''
    words_match = get_english_count(message) * 100 >= word_percentage
    num_letters = len(remove_non_letters(message))
    message_letters_percentage = float(num_letters) / len(message) * 100
    letters_match = message_letters_percentage >= letter_percentage
    return words_match and letters_match