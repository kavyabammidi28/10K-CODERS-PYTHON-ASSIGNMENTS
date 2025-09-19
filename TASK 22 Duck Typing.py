#Duck Typing Tasks
#1. Walk like a Duck
class Duck:
    def walk(self):
        print("Duck is walking like a duck...")

class Person:
    def walk(self):
        print("Person is walking like a human...")

def make_it_walk(obj):
    obj.walk()   # Duck typing: no type checking

# Test
duck = Duck()
person = Person()

make_it_walk(duck)
make_it_walk(person)

#2.Media Player Example
class MP3:
    def play(self):
        print("Playing MP3 music...")

class Video:
    def play(self):
        print("Playing Video...")

def start_media(obj):
    obj.play()   # works for both MP3 and Video

# Test
m = MP3()
v = Video()

start_media(m)
start_media(v)

#3.Payment System
class CreditCard:
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class UPI:
    def pay(self, amount):
        print(f"Paid {amount} using UPI.")

def process_payment(obj, amount):
    obj.pay(amount)

# Test
cc = CreditCard()
upi = UPI()

process_payment(cc, 1000)
process_payment(upi, 500)

#Abstraction Tasks
#4.shape area
from abc import ABC, abstractmethod
import math
class Shape(ABC):
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius

s = Square(5)
c = Circle(3)
print("Square area:", s.area())
print("Circle area:", c.area())

#5.Vehicle start
from abc import ABC, abstractmethod
import math
class Vehicle(ABC):
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

class Bike(Vehicle):
    def start(self):
        print("Bike started")

# Test
car = Car()
bike = Bike()
car.start()
bike.start()

#6.Bank Account
class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance - amount >= 500:
            self.balance -= amount
            print(f"Withdrawn {amount}, New Balance: {self.balance}")
        else:
            print("Insufficient balance! Minimum 500 required.")

class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrawn {amount}, New Balance: {self.balance}")

# Test
s = SavingsAccount(2000)
c = CurrentAccount(1500)
s.withdraw(1000)
c.withdraw(1200)

#7.Report Generation
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

# Test
pdf = PDFReport()
excel = ExcelReport()
pdf.generate()
excel.generate()

#8.Employee Work
class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

class Developer(Employee):
    def work(self):
        print("Writing code")

class Tester(Employee):
    def work(self):
        print("Testing software")

# Test
d = Developer()
t = Tester()
d.work()
t.work()

#9.Appliance Power
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class Fan(Appliance):
    def turn_on(self):
        print("Fan is ON")

class Light(Appliance):
    def turn_on(self):
        print("Light is ON")

# Test
fan = Fan()
light = Light()
fan.turn_on()
light.turn_on()
