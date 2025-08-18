# 1. Print Numbers Except Multiples of 3
print("Numbers from 1 to 50 (excluding multiples of 3):")
for i in range(1, 51):
    if i % 3 == 0:
        continue
    print(i, end=' ')
print("\n")
  

# 2. First Multiple of 11
while True:
    num = int(input("Enter a number (break if multiple of 11): "))
    if num % 11 == 0:
        print(f"{num} is divisible by 11. Exiting loop.")
        break


# 3. Count Vowels in a String
text = input("\nEnter a string to count vowels: ")
count = 0
for char in text.lower():
    if char in 'aeiou':
        count += 1
print(f"Number of vowels: {count}")


# 4. Reverse Even Numbers
print("\nEven numbers from 100 to 2 in reverse:")
num = 100
while num >= 2:
    if num % 2 == 0:
        print(num, end=' ')
    num -= 1
print("\n")


# 5. Password Verification
while True:
    password = input("Enter the password: ")
    if password == "admin123":
        print("Access granted!")
        break
    else:
        print("Incorrect password. Try again.")


# 6. Multiplication Table (1–10)
n = int(input("\nEnter a number for multiplication table: "))
print(f"Multiplication table of {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")


# 7. Skip Negative Numbers (additional clarification)
print("\nEnter numbers (negative numbers will be skipped, enter 0 to stop):")
while True:
    num = int(input("Enter number: "))
    if num == 0:
        break
    if num < 0:
        continue
    print(f"You entered: {num}")


# 8. Sum of N Odd Numbers
N = int(input("\nEnter N to find sum of first N odd numbers: "))
sum_odd = 0
count = 0
num = 1
while count < N:
    sum_odd += num
    num += 2
    count += 1
print(f"Sum of first {N} odd numbers is {sum_odd}")


# 9. List Prime Numbers from 1 to 50
print("\nPrime numbers between 1 and 50:")
for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if not is_prime:
        continue
    print(num, end=' ')
print("\n")

# 10. Running Total Until Zero
total = 0
print("Enter numbers to sum (0 to stop):")
while True:
    num = int(input("Enter number: "))
    if num == 0:
        break
    total += num
print(f"Total sum: {total}")
