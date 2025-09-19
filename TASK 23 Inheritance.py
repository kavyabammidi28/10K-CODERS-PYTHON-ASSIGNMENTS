#Single Inheritance
#1.Bank Account System
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. New Balance: {self.balance}")
        else:
            print("Insufficient funds!")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest added: {interest}. New Balance: {self.balance}")

sa = SavingsAccount(12345, 1000, 5)
sa.deposit(500)
sa.add_interest()
sa.withdraw(300)

#2.Library Management
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def download(self):
        print(f"Downloading '{self.title}' by {self.author} ({self.file_size}MB)...")

ebook = EBook("Python Basics", "Guido van Rossum", 5)
ebook.download()

#3.Employee Management
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

dev = Developer("Alice", 80000, "Python")
print(f"Name: {dev.name}, Salary: {dev.salary}, Language: {dev.programming_language}")


#Multiple Inheritance
#4.Smart phone Features
class Camera:
    def take_photo(self):
        print("Photo taken!")

class MusicPlayer:
    def play_music(self):
        print("Playing music...")

class Smartphone(Camera, MusicPlayer):
    pass

phone = Smartphone()
phone.take_photo()
phone.play_music()
 
#5.Vehicle Features
class Engine:
    def start_engine(self):
        print("Engine started.")

class Wheels:
    def rotate_wheels(self):
        print("Wheels are rotating.")

class Car(Engine, Wheels):
    def drive(self):
        print("Car is driving.")

c = Car()
c.start_engine()
c.rotate_wheels()
c.drive()

#6.Hospital Management
class Doctor:
    def treat_patient(self):
        print("Doctor is treating a patient.")

class Researcher:
    def conduct_research(self):
        print("Researcher is conducting research.")

class DoctorResearcher(Doctor, Researcher):
    pass

dr = DoctorResearcher()
dr.treat_patient()
dr.conduct_research()

#Multi-level inheritance
#7.Educational Hierarchy
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

class HeadOfDepartment(Teacher):
    def __init__(self, name, subject, department_name):
        super().__init__(name, subject)
        self.department_name = department_name

hod = HeadOfDepartment("Dr. Smith", "Physics", "Science Department")
print(f"Name: {hod.name}, Subject: {hod.subject}, Department: {hod.department_name}")

#8.Online Shopping System
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Electronics(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

class Mobile(Electronics):
    def __init__(self, name, price, brand, ram, storage):
        super().__init__(name, price, brand)
        self.ram = ram
        self.storage = storage

m = Mobile("iPhone", 80000, "Apple", "6GB", "128GB")
print(f"Product: {m.name}, Price: {m.price}, Brand: {m.brand}, RAM: {m.ram}, Storage: {m.storage}")

#9.Transport System
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class Car(Vehicle):
    def __init__(self, speed, fuel_type):
        super().__init__(speed)
        self.fuel_type = fuel_type

class ElectricCar(Car):
    def __init__(self, speed, fuel_type, battery_capacity):
        super().__init__(speed, fuel_type)
        self.battery_capacity = battery_capacity

ec = ElectricCar(120, "Electric", "75kWh")
print(f"Speed: {ec.speed} km/h, Fuel: {ec.fuel_type}, Battery: {ec.battery_capacity}")
