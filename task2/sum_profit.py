# Функція яка буде аналізувати текст, ідентифікувати всі дійсні числа, що вважаються частинами доходів, і повертати їх як генератор. 
# Також потрібно реалізувати функцію, яка буде використовувати generator_numbers для підсумовування цих чисел і обчислення загального прибутку.

import re
from typing import Callable

# Function that creates a generator to iterate over all valid numbers in the text
def generator_numbers(text: str):

    # Find all the numbers in the text with surrounding spaces
    numbers = re.findall(r'( \d+.\d+ )', text)

    # Return a generator that iterates over the found numbers
    for number in numbers:
        yield float(number.strip())  # Convert each number to float and remove any surrounding spaces

# Function to calculate the sum of the found numbers
def sum_profit(text: str, func: Callable) -> float:
   
    # Call the generator function to get numbers and sum them
    return sum(func(text))  # Sum up the numbers returned by the generator

# Test function
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")