#SECTION1-Easy while loop tasks
# 1. Print numbers from 1 to 5 using while loop
print("Numbers from 1 to 5:")
i = 1
while i <= 5:
    print(i, end=' ')
    i += 1
print("\n")
 

# 2. Print even numbers from 1 to 10 using while loop
print("Even numbers from 1 to 10:")
i = 1
while i <= 10:
    if i % 2 == 0:
        print(i, end=' ')
    i += 1
print("\n")


# 3. Print sum of numbers from 1 to 10 using while loop
print("Sum of numbers from 1 to 10:")
i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print(total)
print()


# 4. Print each digit of a number using while loop
num = int(input("Enter a number to print each digit: "))
digits = str(num)  # Convert to string for easy iteration
i = 0
while i < len(digits):
    print(digits[i], end=' ')
    i += 1
print("\n")


# 5. Print numbers from 10 down to 1 using while loop
print("Numbers from 10 down to 1:")
i = 10
while i >= 1:
    print(i, end=' ')
    i -= 1
print()



#SECTION 2-FOR Loop Tasks
# 6. Print numbers from 1 to 10 using for loop
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i, end=' ')
print("\n")

# 7. Print each character in the word "banana" using for loop
print("Characters in 'banana':")
for char in "banana":
    print(char, end=' ')
print("\n")

# 8. Print the square numbers from 1 to 5 using for loop
print("Square numbers from 1 to 5:")
for i in range(1, 6):
    print(i**2, end=' ')
print("\n")

# 9. Print all even numbers from list
print("Even numbers from the list [2,5,8,9,10]:")
numbers = [2, 5, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(num, end=' ')
print("\n")

# 10. Print numbers from 1 to 20 that are divisible by 3
print("Numbers from 1 to 20 divisible by 3:")
for i in range(1, 21):
    if i % 3 == 0:
        print(i, end=' ')
print()



#SECTION 3-Nested Loop Tasks

# 11. Star pattern
print("Star Pattern:")
rows = 3
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()
print()



# 12. Number pattern (same row repeated)
print("Number Pattern (same row repeated):")
for i in range(3):   # 3 rows
    for j in range(1, 4):   # Numbers 1 to 3
        print(j, end=" ")
    print()
print()



# 13. Triangle number pattern
print("Triangle Number Pattern:")
rows = 3
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print()

# 14. Multiplication table of 2 (up to 10)
print("Multiplication Table of 2:")
for i in range(1, 11):
    print(f"2 x {i} = {2*i}")
print()



# 15. Print each character of two words in a list
print("Characters in each word from the list:")
words = ["hi", "ok"]
for word in words:
    for char in word:
        print(char, end=" ")
    print()


#Loops with Conditions
# 16. Print numbers from 1 to 10 and print "Even" or "Odd"
print("Numbers with Even/Odd:")
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "Even")
    else:
        print(i, "Odd")
print()

# 17. Ask the user to enter 5 numbers and print only even numbers
print("Enter 5 numbers:")
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        print(f"{num} is Even")
print()

# 18. Ask the user to enter numbers until they enter a negative number, then stop
print("Enter numbers (negative number to stop):")
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Negative number entered. Stopping.")
        break
    print(f"You entered: {num}")
print()

# 19. Print vowels in a word using for loop and if condition
word = input("Enter a word to print vowels: ")
print("Vowels in the word:")
for char in word.lower():
    if char in "aeiou":
        print(char, end=" ")
print("\n")

# 20. Count how many vowels are there in a given word
word = input("Enter a word to count vowels: ")
count = 0
for char in word.lower():
    if char in "aeiou":
        count += 1
print(f"Number of vowels: {count}")
  



#SECTION 5:Creative and Fun Loops
# 21. Print the word "Hello" 5 times using a loop
print("Task 21: Print 'Hello' 5 times")
for i in range(5):
    print("Hello")
print()

# 22. Ask the user their favorite colour 3 times using a loop
print("Task 22: Ask favorite colour 3 times")
for i in range(3):
    color = input(f"Enter your favorite color ({i+1}/3): ")
    print(f"You entered: {color}")
print()

# 23. Print pattern using nested loop: A, BB, CCC
print("Task 23: Pattern A, BB, CCC")
for i in range(1, 4):
    print(chr(64 + i) * i)  # chr(65) is 'A'
print()

# 24. Count how many times 'a' appears in 'banana'
print("Task 24: Count 'a' in 'banana'")
word = "banana"
count_a = 0
for char in word:
    if char == 'a':
        count_a += 1
print(f"'a' appears {count_a} times in '{word}'")
print()

# 25. Print numbers from 1 to 10, print 'small' if <5, else 'big'
print("Task 25: Numbers with small/big")
for i in range(1, 11):
    if i < 5:
        print(i, "small")
    else:
        print(i, "big")
