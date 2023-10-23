from common import (
    get_number_from_input,
    get_percentage_from_input,
    calculate_down_payment_time,
)


user_salary = get_number_from_input("Enter your salary: ")
desired_duration = (
    get_percentage_from_input("Enter your desired down payment duration in years: ")
    * 12
)
salary_growth = get_number_from_input("Enter your planned salary increase: ")
price_of_real_estate = get_number_from_input("Enter the price of real estate: ")
down_payment_percentage = get_percentage_from_input(
    "Enter the percent of down payment: "
)
investments_percentage = get_number_from_input("Enter the percent of investments: ")


ALLOWED_MONTH_DIFFERENCE = 1
down_payment = price_of_real_estate * down_payment_percentage / 100
lower_percent_of_savings = 0
upper_percent_of_savings = 100
percent_of_savings = None
months_needed = None

best_saving_time = calculate_down_payment_time(
    user_salary,
    100,
    salary_growth,
    down_payment,
    investments_percentage,
)

if best_saving_time > desired_duration:
    print("You can't pay the down payment in your desired duration")
    exit()

while (
    not months_needed
    or abs(months_needed - desired_duration) > ALLOWED_MONTH_DIFFERENCE
):
    percent_of_savings = (lower_percent_of_savings + upper_percent_of_savings) / 2
    months_needed = calculate_down_payment_time(
        user_salary,
        percent_of_savings,
        salary_growth,
        down_payment,
        investments_percentage,
    )

    if months_needed > desired_duration:
        lower_percent_of_savings = percent_of_savings
    else:
        upper_percent_of_savings = percent_of_savings


print(
    f"To reach your desired down payment duration of {desired_duration / 12} years, you should save {percent_of_savings:.1f}% of your salary each month."
)
