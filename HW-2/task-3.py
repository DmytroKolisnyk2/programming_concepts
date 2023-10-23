import math
from common import (
    get_number_from_input,
    get_percentage_from_input,
    get_year_month_string,
)

price_of_real_estate = get_number_from_input("Enter the price of real estate: ")
down_payment_percentage = get_percentage_from_input(
    "Enter the percent of down payment: "
)
credit_percentage_rate = get_percentage_from_input("Enter the credit percentage rate: ")
comfortable_monthly_payment = get_number_from_input(
    "Enter your comfortable monthly payment: "
)
investments_percentage = get_number_from_input("Enter the percent of investments: ")

down_payment = price_of_real_estate * down_payment_percentage / 100
saved_down_payment = 0
month_count = 0

while saved_down_payment < down_payment:
    month_count += 1
    saved_down_payment *= 1 + investments_percentage / (12 * 100)
    saved_down_payment += comfortable_monthly_payment

print(f"It will take {get_year_month_string(month_count)} for the down payment")

payed_credit = price_of_real_estate - down_payment
current_credit = price_of_real_estate

# formula taken from task-1_2.py 35-38 lines
credit_term_years = ((price_of_real_estate - down_payment)) / (
    12 * comfortable_monthly_payment
    - price_of_real_estate * credit_percentage_rate / 100
)
credit_term_months = math.ceil(credit_term_years * 12)

print(f"It will take {get_year_month_string(credit_term_months)} to pay the credit")
