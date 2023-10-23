from common import (
    get_number_from_input,
    get_percentage_from_input,
    get_year_month_string,
    exit_on_input_confirmation,
)

user_salary_input = get_number_from_input("Enter your salary: ")
percent_of_savings = get_percentage_from_input(
    "Enter percentage of money you is willing to save: "
)
salary_growth = get_number_from_input("Enter your planned salary increase: ")
price_of_real_estate = get_number_from_input("Enter the price of real estate: ")
down_payment_percentage = get_percentage_from_input(
    "Enter the percent of down payment: "
)
investments_percentage = get_number_from_input("Enter the percent of investments: ")

user_salary = user_salary_input
down_payment = price_of_real_estate * down_payment_percentage / 100
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

print(f"It will take {get_year_month_string(month_count)} for the down payment")

exit_on_input_confirmation()

percent_of_savings = get_percentage_from_input(
    "Enter percentage of money you is willing to save: "
)
credit_percentage_rate = get_percentage_from_input("Enter the credit percentage rate: ")

credit_repayment_term = 0
credit_repayment = 0
real_estate_growth = 1 + credit_percentage_rate * credit_repayment_term / (12 * 100)

while credit_repayment < price_of_real_estate * real_estate_growth - down_payment:
    credit_repayment_term += 1
    credit_repayment += monthly_savings
    real_estate_growth = 1 + credit_percentage_rate * credit_repayment_term / (12 * 100)

    if (credit_repayment_term + month_count) % 6 == 0:
        user_salary += salary_growth
        monthly_savings = user_salary * percent_of_savings / 100

print(f"It will take {get_year_month_string(credit_repayment_term)} to pay the credit")
