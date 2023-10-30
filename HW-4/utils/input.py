MIN_BASE = 2
MAX_BASE = 16

ALLOWED_PREFIXES = ("0b", "0x")
PREFIXES_BASE_DICT = {"0b": 2, "0x": 16}


def format_number(number, base):
    return f"{number}x{base}".lower()


def has_prefixes(number):
    if number.startswith(ALLOWED_PREFIXES):
        try:
            number_part = number[2:]
            prefix = number[:2]

            int(number_part, PREFIXES_BASE_DICT[prefix])
            formatted_number = format_number(number_part, PREFIXES_BASE_DICT[prefix])
            return formatted_number

        except ValueError:
            return print("Wrong number format after prefix")


def has_separator(number):
    separator_index = number.find("x")

    if separator_index != -1:
        try:
            base_part = int(number[separator_index + 1 :])

            if base_part < MIN_BASE or base_part > MAX_BASE:
                return print(f"Base must be between {MIN_BASE} and {MAX_BASE}")

            number_part = number[:separator_index]
            int(number_part, int(base_part))
            return number
        except ValueError:
            return print("Wrong number format before prefix or after base")


def is_decimal(number):
    if not number.isdecimal():
        return print("Number is not decimal or in format ob/0x/xN")

    return format_number(number, 10)


def get_valid_number(message):
    while True:
        number = input(message)

        has_prefixes_result = has_prefixes(number)
        if has_prefixes_result:
            return has_prefixes_result

        has_separator_result = has_separator(number)
        if has_separator_result:
            return has_separator_result

        is_decimal_result = is_decimal(number)
        if is_decimal_result:
            return is_decimal_result


def ask_translating_format(message):
    while True:
        try:
            translating_format = int(input(message))
            if translating_format < MIN_BASE or translating_format > MAX_BASE:
                print(f"Base must be between {MIN_BASE} and {MAX_BASE}")
                continue
            return translating_format
        except ValueError:
            print("Translating format must be a number")


def exit_on_input_confirmation():
    confirmation_answers = frozenset(["y", "yes", "n", "no"])
    confirmation_value = None

    while True:
        confirmation_value = input("Do you want to start again? (y/n): ").lower()
        if confirmation_value in confirmation_answers:
            break
        else:
            print("Please enter yes/no or y/n")

    if confirmation_value in frozenset(["n", "no"]):
        exit()
