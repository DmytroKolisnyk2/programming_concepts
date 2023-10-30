from utils import (
    get_valid_number,
    exit_on_input_confirmation,
    ask_translating_format,
    translate_number,
)


def app():
    while True:
        number = get_valid_number("Enter a number: ")
        translating_format = ask_translating_format("Enter translating format: ")
        print(translate_number(number, translating_format))
        exit_on_input_confirmation()


app()
