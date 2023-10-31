import words_fetcher, random

ALLOWED_CHARS = "abcdefghijklmnopqrstuvwxyz"
ALLOWED_MISTAKES = 8
WORD_LENGTH = 6
WORDS = words_fetcher.fetch_words(WORD_LENGTH)
WORD = random.choice(WORDS)

guessed_letters = set()
mistakes_count = 0

print(f"Welcome to Hangman!")


def get_guessed_word():
    result = ""
    for letter in WORD:
        if letter in guessed_letters:
            result += letter
        else:
            result += "."
    return result


def get_input_letter():
    while True:
        letter = input(f"The word is: {get_guessed_word()}\nEnter a letter: ")
        if letter in ALLOWED_CHARS:
            return letter
        else:
            print("Letter must be a lowercase English letter.")


def attempt_letter(guessed_word):
    letter = get_input_letter()
    if letter in guessed_word:
        print("You already guessed this letter!")
        return

    if letter in WORD:
        print("Correct!")
        guessed_letters.add(letter)
        return

    print(f"No such letter! {mistakes_count + 1}/{ALLOWED_MISTAKES} mistakes")
    return mistakes_count + 1


while mistakes_count < ALLOWED_MISTAKES:
    updated_mistakes_count = attempt_letter(get_guessed_word())
    if updated_mistakes_count:
        mistakes_count = updated_mistakes_count
    if get_guessed_word() == WORD:
        print(f"Congratulations, you guessed the word!. The word was {WORD}")
        exit()

print(f'You lost. The word was "{WORD}".')
