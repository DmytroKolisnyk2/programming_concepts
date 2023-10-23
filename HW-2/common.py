def get_number_from_input(asking_text):
    while True:
        try:
            number = float(input(asking_text))
            return number
        except ValueError:
            print("Please enter a number")


def get_percentage_from_input(asking_text):
    while True:
        try:
            number = get_number_from_input(asking_text)
            if number < 0 or number > 100:
                raise ValueError
            return number
        except ValueError:
            print("Please enter a number between 0 and 100")


def get_year_month_string(month_count):
    years = month_count // 12
    months = month_count % 12
    if years == 0:
        return f"{months} months"
    elif years == 1:
        return f"{years} year and {months} months"
    else:
        return f"{years} years and {months} months"


def exit_on_input_confirmation():
    confirmation_answers = frozenset(["y", "yes", "n", "no"])
    confirmation_value = None

    while True:
        confirmation_value = input(
            "Do you want to calculate body of credit? (y/n): "
        ).lower()
        if confirmation_value in confirmation_answers:
            break
        else:
            print("Please enter yes/no or y/n")

    if confirmation_value in frozenset(["n", "no"]):
        exit()


def calculate_down_payment_time(
    user_salary_arg,
    percent_of_savings,
    salary_growth,
    down_payment,
    investments_percentage,
):
    user_salary = user_salary_arg
    monthly_savings = user_salary * percent_of_savings / 100
    saved_down_payment = 0
    month_count = 0

    while saved_down_payment < down_payment:
        month_count += 1
        saved_down_payment *= 1 + investments_percentage / (12 * 100)
        saved_down_payment += monthly_savings

        if (month_count) % 6 == 0:
            user_salary += salary_growth
            monthly_savings = user_salary * percent_of_savings / 100

    return month_count
