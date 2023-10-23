import datetime

(name, age) = input('Enter your name & age with whitespaces: \n').split()

age = int(age)

current_year = datetime.datetime.now().year
birth_year = current_year - age

print(f"Hello, {name}! You are {age} years old, so you was born in year {birth_year}")
