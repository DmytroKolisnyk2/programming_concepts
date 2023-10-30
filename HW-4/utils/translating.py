CHARS = "0123456789abcdef"


def get_digit(number):
    if type(number) == int:
        return CHARS[number]

    return CHARS.find(number)


def translate_to_decimal(number, base):
    decimal_number = 0

    for i in range(len(number)):
        digit = get_digit(number[i])
        place = len(number) - i - 1
        decimal_number += digit * base**place

    return decimal_number


def translate_number(number, translating_format):
    separator_index = number.find("x")
    number_part = number[:separator_index]
    base_part = int(number[separator_index + 1 :])

    decimal_whole = translate_to_decimal(number_part, base_part)
    translated_number = ""

    while not decimal_whole == 0:
        translated_number += get_digit(decimal_whole % translating_format)
        decimal_whole //= translating_format

    return translated_number[::-1].upper()
