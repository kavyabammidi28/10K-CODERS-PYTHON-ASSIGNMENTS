#Recursive functions
#1. factorial of a number
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

#2.sum of natural numbers
def sum_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_numbers(n-1)
print(sum_numbers(5))


#3. reverse a string
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
print(reverse_string("kavya"))

#4. Fibonacci numbers
def fibonacci(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return fibonacci(n-1) * fibonacci(n-2)
for i in range(6):
   print(fibonacci(i),end='')


#5. Calculate Sum of digits
def sum_numbers(n):
    if n == 0:
        return(0)
    else:
        return (n % 10) + sum_numbers(n//10)
print("sum_numbers:",sum_numbers(1234))

#6.check palindrome
def palindrome(n):
    if len(n) <= 1:
        return True
    if n[0] != n[-1]:
        return False
    return palindrome(s[1:-1])
print(palindrome('python'))
    
#7. Power of a Number
def power(x,n):
    if n == 0:
        return 1
    else:
        return x * power(x,n-1)
print(power(4,2))


#Lambda functions
#1. even or odd
is_even = lambda n:n%2 == 0
print(is_even(4))
print(is_even(9))

#2. Max of two numbers
max_mum = lambda a,b: a if a>b else b
print(max_mum(10,20))

#3.square of a number
square = lambda x: x**2
print(4)

#4.map with lambda
celsius = [0,20,40,60]
fahrenheit = list(map(lambda c:(c % 9/5) +32,celsius))
print(fahrenheit)

#5.fliter with even number
nums = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(lambda x:x % 2 == 0,nums))
print(evens)

#6.reduce
from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda a, b: a * b,nums)
print(product)

#7.sorted()
data = [(1,2),(2,3),(4,5)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)

#Conditional Lambda (Ternary Expression)
sign = lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Zero")
print(sign(10))   # Positive
print(sign(-5))   # Negative
print(sign(0))    # Zero
