import words_fetcher, random

ALLOWED_ATTEMPTS = 6
WORD_LENGTH = 5
WORDS = words_fetcher.fetch_words(WORD_LENGTH, WORD_LENGTH)
WORD = random.choice(WORDS)

print(f"Welcome to Wordle! Allowed words are: \n{', '.join(WORDS)}")


def get_input_word(attempt_count):
    while True:
        word = input(f"Attempt #{attempt_count}. Enter a word: ")
        if word in WORDS:
            return word
        else:
            print("Word must be in allowed words list.")


def attempt_word(guessed_word, attempt_count):
    word = get_input_word(attempt_count)
    if word == guessed_word:
        print("Congratulations, you guessed the word!")
        exit()

    word_list = word
    hint = ""

    for i in range(len(word_list)):
        if word_list[i] == guessed_word[i]:
            hint += word_list[i].upper()
        elif word_list[i] in guessed_word:
            hint += word_list[i] + "*"
        else:
            hint += word_list[i]
        hint += " "

    print(hint)


for i in range(ALLOWED_ATTEMPTS):
    attempt_word(WORD, i + 1)

print(f'You lost. The word was "{WORD}".')
