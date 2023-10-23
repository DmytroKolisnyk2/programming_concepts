from common import (
    get_number_from_input,
    get_percentage_from_input,
    get_year_month_string,
    exit_on_input_confirmation,
)

user_salary = get_number_from_input("Enter your salary: ")
percent_of_savings = get_percentage_from_input(
    "Enter percentage of money you is willing to save: "
)
price_of_real_estate = get_number_from_input("Enter the price of real estate: ")
down_payment_percentage = get_percentage_from_input(
    "Enter the percent of down payment: "
)
investments_percentage = get_number_from_input("Enter the percent of investments: ")

down_payment = price_of_real_estate * down_payment_percentage / 100
monthly_savings = user_salary * percent_of_savings / 100
saved_down_payment = 0
month_count = 0

while saved_down_payment < down_payment:
    month_count += 1
    saved_down_payment *= 1 + investments_percentage / (12 * 100)
    saved_down_payment += monthly_savings

print(f"It will take {get_year_month_string(month_count)} for the down payment")

exit_on_input_confirmation()

credit_term = get_number_from_input("Enter the credit term in years: ")
credit_percentage_rate = get_percentage_from_input("Enter the credit percentage rate: ")

credit_total_value = price_of_real_estate * (
    1 + (credit_percentage_rate * credit_term) / 100
)
monthly_credit_payment = (credit_total_value - down_payment) / (credit_term * 12)

if monthly_credit_payment > user_salary:
    print("You can't afford this credit with your current salary")
else:
    print(f"Your monthly credit payment will be {monthly_credit_payment}")
