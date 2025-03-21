# Функція яка створює та використовує кеш для зберігання і повторного використання вже обчислених значень чисел Фібоначчі.

from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
   
    # Create an empty dictionary to store cached numbers
    cache = {}
    
    def fibonacci(n: int) -> int:
       
        # If number is already in the cache, return it
        if n in cache:
            return cache[n]
        
        # Base cases: Fibonacci(0) = 0, Fibonacci(1) = 1
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        # If the number is not in the cache, calculate it recursively
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]

    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610