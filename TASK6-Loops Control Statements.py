
# TASKS ON break


# 1. Find the first even number
def first_even_number(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num  
    return None  
nums = [1, 3, 5, 8, 11]
print("First even number:", first_even_number(nums))
print()


# 2. Password validation with retries
correct_password = "admin123"
attempts = 0
while attempts < 3:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted")
        break
    attempts += 1
else:
    print("Locked out")
print()


# 3. Infinite loop exit
while True:
    user_input = input("Type something (type 'exit' to stop): ")
    if user_input.lower() == "exit":
        print("Exiting loop...")
        break
    print("You entered:", user_input)
print()




# TASKS ON  continue

# 4. Skip negative numbers
numbers = [3, -2, 7, -5, 10, -1]
print("Positive numbers from the list:")
for num in numbers:
    if num < 0:
        continue
    print(num)
print()


# 5. Skip vowels
word = "education"
print("Consonants in the word:")
for char in word.lower():
    if char in "aeiou":
        continue
    print(char, end=" ")
print("\n")


# 6. Divisible by 3 but not 5
print("Numbers from 1 to 50 divisible by 3 but not by 5:")
for i in range(1, 51):
    if i % 3 == 0 and i % 5 != 0:
        print(i, end=" ")
print()


# TASKS ON pass

# 7. Define placeholder function
def process_data():
    pass  # Will implement later

# 8. Skeleton class
class User:
    pass  # Functionality will be added later

# 9. Use pass in empty loop
for i in range(1, 6):
    pass  



# MIXED CHALLENGES

# 10. Filter and stop
numbers = [0, 12, 45, 0, 60, 22, 0, 15, 48, 50, 10]
print("Filtered numbers:")
for num in numbers:
    if num == 0:
        pass  # Ignore zero
    elif num % 2 != 0:
        continue  # Skip odd numbers
    elif num >= 50:
        break  # Stop if number is >= 50
    print(num)
print()



# 11. Word filter loop
words = ['hi', 'cat', 'wait', 'dog', 'end', 'zebra']
print("Filtered words:")
for word in words:
    if len(word) < 3:
        continue  # Skip short words
    elif word == 'wait':
        pass  # Do nothing
    elif word == 'end':
        break  # Stop the loop
    print(word)

