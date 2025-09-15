#Section A:
#1. A class in Python is a blueprint for creating objects (instances) that encapsulate
# data (attributes) and methods (functions).
class Car:
    def start(self):
        print("Car started")

# Creating an object of class
my_car = Car()   # object creation
my_car.start()

#2.
# break: Terminates the loop completely and transfers control to the next statement after the loop.
# continue: Skips the current iteration and moves to the next iteration of the loop.
# pass: A null statement that does nothing. It is used as a placeholder.

#3. Syntax:
# if condition1:
# elif condition2:    
# else:
    
# Example:
x = 10
if x > 20:
    print("Greater than 20")
elif x == 10:
    print("Equal to 10")
else:
    print("Less than 10")

#4.The __init__() method is a constructor in Python classes.
#It is automatically called when an object is created and is used to initialize the object’s attributes.
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

s1 = Student("Kavya", 101)   # __init__() is called automatically


#5.
def square(num):
   return num * num
# Example usage
print(square(5))  

#SECTION B:
#6.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def showDetails(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Creating two objects
car1 = Car("Tesla", "Model S")
car2 = Car("BMW", "X5")

car1.showDetails()
car2.showDetails()

#7.
def check_even_odd(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

# Example usage
check_even_odd(7)
check_even_odd(12)

#8.
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

#9.
num = int(input("Enter a number: "))

if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")

#10.
num = int(input("Enter a number: "))
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num = num // 10

print("Sum of digits:", sum_digits)


#SECTION C:
#11.
for i in range(1, 6):       # rows
    for j in range(i):      # columns
        print("*", end=" ")
    print()

#12.
print("Prime numbers between 1 and 50:")

for num in range(2, 51):       # check numbers from 2 to 50
    is_prime = True
    for i in range(2, num):    # check divisibility
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")


#SECTION D:
#14.
for i in range(1, 21):
    if i % 3 == 0:
        continue   # skip multiples of 3
    print(i, end=" ")

#15.
for i in range(1, 11):
    if i == 7:
        break   # stop when i is 7
    print(i, end=" ")

#16.
for i in range(1, 6):          
    for j in range(1, 2*i):    
        if j % 2 == 0:        
            continue
        print(j, end=" ")
    print()   


#SECTION E:
#17.
class Student:
    def __init__(self):
        self.name = ""
        self.roll_no = 0
        self.marks = 0

    # Method to accept student details
    def acceptDetails(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    # Method to calculate grade
    def calculateGrade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        else:
            return "C"

    # Method to display student details
    def displayDetails(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}, Grade: {self.calculateGrade()}")


# Creating 3 Student objects
s1 = Student()
s2 = Student()
s3 = Student()

s1.acceptDetails("Kavya", 101, 92)
s2.acceptDetails("Rahul", 102, 80)
s3.acceptDetails("Meena", 103, 65)

# Display details
s1.displayDetails()
s2.displayDetails()
s3.displayDetails()

#18.
# Function to check prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# Accept a number from user
n = int(input("Enter a number: "))

if is_prime(n):
    print(n, "is a Prime number.")
    print("Prime numbers up to", n, "are:")
    for i in range(2, n+1):
        if is_prime(i):
            print(i, end=" ")
else:
    print(n, "is NOT a Prime number.")


