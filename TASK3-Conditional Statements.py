# Check if a number is divisible by both 3 and 5
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5.")
else:
    print(f"{num} is NOT divisible by both 3 and 5.")



# Compare two numbers and print which one is greater
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(f"{a} is greater than {b}")
elif b > a:
    print(f"{b} is greater than {a}")
else:
    print("Both numbers are equal")


# Ask for marks and print grade
marks = int(input("Enter your marks (0–100): "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")


# Check whether number is positive or even using 'or'
num = int(input("Enter a number: "))

if num > 0 or num % 2 == 0:
    print(f"{num} is either positive or even (or both).")
else:
    print(f"{num} is neither positive nor even.")


# Ask for user's age and classify
age = int(input("Enter your age: "))

if age < 13:
    print("You are a Child.")
elif age >= 13 and age <= 19:
    print("You are a Teen.")
else:
    print("You are an Adult.")
