#TASK ON DATA TYPES

#Task 1: Swap Two Numbers -Swap using a temporary variable and tuple unpacking
# swaping using temporary variables
a = 10
b = 5
c = 0

c = a
a = b
b = c

print('a:',a,'b:',b)
 

# swaping using tuple unpacking
d = 6
e = 9
d,e = e,d
print('d:',d,'e:',e)


#Task 2: Identify Data Types
#Input three values from the user and print their types
n1 = input('Enter a Value:')
n2 = input('Enter a Value:')
n3 = input('Enter a Value:')
print(type(n1),type(n2),type(n3))



#Task 3: Simple Calculator
#Perform +, -, *, /, //, %, **
# Task 3: Simple Calculator
# Perform +, -, *, /, //, %, **

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = input("Enter desired operation (+, -, *, /, //, %, **): ")

if c == "+":
    print("Result:", a + b)
elif c == "-":
    print("Result:", a - b)
elif c == "*":
    print("Result:", a * b)
elif c == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero!")
elif c == "//":
    if b != 0:
        print("Result:", a // b)
    else:
        print("Error: Division by zero!")
elif c == "%":
    if b != 0:
        print("Result:", a % b)
    else:
        print("Error: Division by zero!")
elif c == "**":
    print("Result:", a ** b)
else:
    print("Invalid operation!")


#Task 4: Salary Hike
#Take salary and apply 15% hike. Print old and new salary
salary = int(input('Enter your current salary: '))
hike = 0.15 * salary
new_salary = salary + hike

print(f"Old Salary: {salary}")
print(f"New Salary after 15% hike: {new_salary}")



#Task 5: Area and Perimeter of Circle
#Use radius to calculate area and perimeter (pi = 3.14159).
r = int(input('Enter radius of the Desired Circle:'))
pi = 3.14159
perimeter = 2*pi*r
area = pi*(r**2)
print('Area of the circle:', area, 'Perimeter of the circle:',perimeter)



#Task 6: ASCII Character
#Input a character and print its ASCII using ord().
# ord() → Returns the ASCII (or Unicode) value of a character
# Example: ord('A') → 65

# chr() → Returns the character for a given ASCII (or Unicode) value
# Example: chr(65) → 'A'

n = input('Enter a Character:')
asc = ord(n)
print(f"The ASCII value of '{n}' is: {asc}")



#Task 7: Check Even or Odd
#Use modulus operator to determine if a number is even or odd.
n = int(input('Enter a Number:'))
if n % 2 == 0:
        print('n is even')
else:
        print('n is odd')


#Task 8: Compound Assignment Practice
#Use +=, -=, =, //=, %= operators on a variable. Show result after each.
a = 123
print(a)
a += 10
print(a)
a -=10
print(a)
a *= 10
print(a)
a //= 10
print(a)
a %= 10
print(a)


#Task 9: Boolean and Logical Check
#Use logical operators to check age and name validity.
age = int(input('Enter Your age:'))
name = input('Enter Your name:')
if age >= 18:
    print(f'hey {name} are a major')
else:
    print(f'hey {name} are a major')


#Perform left shift and right shift by 1 and 2. Explain changes mathematically.
n = int(input("Enter a number: "))
left1 = n << 1  
left2 = n << 2  
right1 = n >> 1
right2 = n >> 2  
print("Left shift by 1:", left1)
print("Left shift by 2:", left2)
print("Right shift by 1:", right1)
print("Right shift by 2:", right2)


#Task 11: Bitwise AND, OR, XOR, NOT
#Use a 12, b = 5 to demonstrate &, |, ^, ~ operators.
# Bitwise Operations in Python
# Given numbers
a = 12  # Binary: 1100
b = 5   # Binary: 0101

a = 12
b = 5
print(a & b)
print(a | b)
print(a ^ b)
print(~b)
print(~a)

# string to int
a = int("25")
print(a, type(a))

# float to string
b = str(12.75)
print(b, type(b))

# int to bool
c = bool(0000)
print(c, type(c))


#Task 13 Temperature Conversion
#Convert Celsius to Fahrenheit and vice versa
# Celsius to Farenheit
c = int(input('Enter a Value'))
f = c * (9/5) + 32 
print(f)
# Farenheit to Celsius
c = (f - 32) * 5/9 
print(c)


#Task 14: Quotient and Remainder -Use // and % to get quotient and remainder Check divisibility
# divident = divisor * quotient + remainder
a = 15
b = 3

print("Quotient:", a // b)
print("Remainder:", a % b)

if a % b == 0:
    print(a, "is divisible by", b)
else:
    print(a, "is not divisible by", b)


#Task 15: String Operations
#Use string methods: upper(), lower(), len(), and 'in'.
str = "Hi KavyA"
print(str.upper(), str.lower(), len(str))
print("KavyA" in str)
print("Hello" in str)   


#Task 16: Sum of Digits
#Input 3-digit number and sum digits using // and % only.
n = int(input("Enter a 3-digit number: "))
sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n //= 10
print("Sum of digits:", sum)


#Task 17: Identity vs Equality
#Use and is with two lists to compare.
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
# Equality check
print("list1 == list2:", list1 == list2)   
print("list1 == list3:", list1 == list3)   
# Identity check
print("list1 is list2:", list1 is list2)   
print("list1 is list3:", list1 is list3)  


#Task 18: Age in Months and Days Convert age in years to months and days.
ay = int(input("Enter your age in years: "))
am = ay * 12
ly = ay // 4
ad = (ay * 365) + ly

print("Age in months:", am)
print("Age in days (approx, considering leap years):", ad)



#Task 20: Bitwise Practice (No bin()) Use a number n and show n, n << 1. n >> 2. Expl#ain mathematically.
n = int(input("Enter a number: "))

print("Original number (n):", n)
print("n << 1 (multiply by 2):", n << 1)
print("n >> 2 (divide by 4):", n >> 2)

