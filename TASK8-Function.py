# 1. Function that returns cube of a number
def cube(num):
    return num ** 3

# 2. Function that takes two numbers and returns their average
def average(a, b):
    return (a + b) / 2

# 3. Function that returns both square and cube of a number
def square_and_cube(num):
    return num ** 2, num ** 3   

# 4. Function is_odd(n) that returns True if odd, else False
def is_odd(n):
    return n % 2 != 0

# 5. Function sum_digits(n) that returns sum of digits
def sum_digits(n):
    return sum(int(digit) for digit in str(abs(n)))  


# 6. Function greet with default parameter
def greet(name='guest'):
    return f"Hello, {name}!"

# 7. Function power with default exponent
def power(base, exponent=2):
    return base ** exponent

# 8. Function total_bill with default values
def total_bill(item='sandwich', quantity=1, price=50):
    return f"Total price for {quantity} {item}(s): ₹{quantity * price}"

# 9. Function employee_info with default parameters
def employee_info(name, age=30, department='HR'):
    return f"Name: {name}, Age: {age}, Department: {department}"

# 10. Function circle_area with default radius
def circle_area(radius=1):
    return 3.14 * radius * radius

# 11. Function to return sum of all even numbers up to a given number
def sum_even_numbers(limit):
    total = 0
    for num in range(2, limit + 1, 2):  # start from 2, step by 2
        total += num
    return total

# 12. Function to return the largest number from a list
def largest_number(numbers):
    if not numbers:  # handle empty list
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


# 13. Function that returns min and max values from a list
def min_max(numbers):
    if not numbers:  # handle empty list
        return None, None
    return min(numbers), max(numbers)

# 14. Function that returns student name, total marks, and average marks
def student_summary(name, marks):
    total = sum(marks)
    average = total / len(marks) if marks else 0
    return name, total, average


# 15. Function to perform basic calculations with a default operator '+'
def calculate(num1, num2, operator='+'):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"



