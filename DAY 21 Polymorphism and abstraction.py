# 1. Animals Speak
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]
for a in animals:
    a.sound()

print("\n--- Calculator Operations ---")

# 2. Calculator Operations
class Calculator:
    def calculate(self, a, b):
        pass

class Add(Calculator):
    def calculate(self, a, b):
        return a + b

class Subtract(Calculator):
    def calculate(self, a, b):
        return a - b

calc1 = Add()
calc2 = Subtract()
print("Addition:", calc1.calculate(10, 5))
print("Subtraction:", calc2.calculate(10, 5))

print("\n--- Transport Ride Fare ---")

# 3. Transport Ride Fare
class Transport:
    def fare(self, distance):
        pass

class Bus(Transport):
    def fare(self, distance):
        return distance * 10

class Train(Transport):
    def fare(self, distance):
        return distance * 5

distance = 20
t1 = Bus()
t2 = Train()
print("Bus Fare:", t1.fare(distance))
print("Train Fare:", t2.fare(distance))

print("\n--- Shape Area ---")

# 4. Shape Area
import math

class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return math.pi * self.r * self.r

shapes = [Square(5), Circle(3)]
for s in shapes:
    print("Area:", s.area())

print("\n--- Employee Work ---")

# 5. Employee Work
class Employee:
    def work(self):
        pass

class Developer(Employee):
    def work(self):
        print("Writing code")

class Tester(Employee):
    def work(self):
        print("Testing software")

e1 = Developer()
e2 = Tester()
e1.work()
e2.work()


from abc import ABC, abstractmethod

print("\n--- Vehicle Start ---")

# 6. Vehicle Start
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

class Bike(Vehicle):
    def start(self):
        print("Bike started")

v1 = Car()
v2 = Bike()
v1.start()
v2.start()


print("\n--- Bank Account ---")

# 7. Bank Account
class BankAccount(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        print(f"Withdrawn {amount} from savings account")

class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        print(f"Withdrawn {amount} from current account")

b1 = SavingsAccount()
b2 = CurrentAccount()
b1.withdraw(500)
b2.withdraw(1000)


print("\n--- Device Power ---")

# 8. Device Power
class Device(ABC):
    @abstractmethod
    def power_on(self):
        pass

class TV(Device):
    def power_on(self):
        print("TV is ON")

class Laptop(Device):
    def power_on(self):
        print("Laptop is ON")

d1 = TV()
d2 = Laptop()
d1.power_on()
d2.power_on()


print("\n--- Student Exam ---")

# 9. Student Exam
class Exam(ABC):
    @abstractmethod
    def start_exam(self):
        pass

class MathExam(Exam):
    def start_exam(self):
        print("Math exam started")

class EnglishExam(Exam):
    def start_exam(self):
        print("English exam started")

s1 = MathExam()
s2 = EnglishExam()
s1.start_exam()
s2.start_exam()


print("\n--- Report Generation ---")

# 10. Report Generation
class Report(ABC):
    @abstractmethod
    def generate(self):
        pass

class PDFReport(Report):
    def generate(self):
        print("PDF Report generated")

class ExcelReport(Report):
    def generate(self):
        print("Excel Report generated")

r1 = PDFReport()
r2 = ExcelReport()
r1.generate()
r2.generate()
