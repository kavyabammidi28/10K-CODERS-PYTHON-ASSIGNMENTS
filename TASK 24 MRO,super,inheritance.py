#Hierarchical Inheritance
# 1. Employee Details
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        print(f"Name: {self.name}, ID: {self.emp_id}")

class Developer(Employee):
    def __init__(self, name, emp_id, programming_language):
        super().__init__(name, emp_id)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")

class Manager(Employee):
    def __init__(self, name, emp_id, team_size):
        super().__init__(name, emp_id)
        self.team_size = team_size

    def display(self):
        super().display()
        print(f"Team Size: {self.team_size}")

dev = Developer("Alice", 101, "Python")
mgr = Manager("Bob", 102, 5)
dev.display()
mgr.display()


# 2. Shapes Area
import math
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

rect = Rectangle(5, 3)
circle = Circle(4)
print("Rectangle Area:", rect.area())
print("Circle Area:", circle.area())


# 3. Vehicle Information
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors

    def display(self):
        print(f"Car: {self.brand}, Year: {self.year}, Doors: {self.doors}")

class Bike(Vehicle):
    def __init__(self, brand, year, bike_type):
        super().__init__(brand, year)
        self.bike_type = bike_type

    def display(self):
        print(f"Bike: {self.brand}, Year: {self.year}, Type: {self.bike_type}")

car = Car("Toyota", 2020, 4)
bike = Bike("Yamaha", 2021, "Sport")
car.display()
bike.display()

#Hybrid Inheritance
# 4. Student Performance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

class Sports:
    def __init__(self, sport_name):
        self.sport_name = sport_name

class CollegeStudent(Student, Sports):
    def __init__(self, name, age, roll_no, sport_name, course):
        Student.__init__(self, name, age, roll_no)
        Sports.__init__(self, sport_name)
        self.course = course

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll No: {self.roll_no}, Sport: {self.sport_name}, Course: {self.course}")

cs = CollegeStudent("Kavya", 20, 101, "Basketball", "B.Tech")
cs.display()


# 5. Teaching Staff
class Staff:
    def __init__(self, name):
        self.name = name

class Teacher(Staff):
    def teach(self):
        print(f"{self.name} is teaching.")

class Researcher(Staff):
    def research(self):
        print(f"{self.name} is researching.")

class Professor(Teacher, Researcher):
    def guide(self):
        print(f"{self.name} is guiding students.")

prof = Professor("Dr. Smith")
prof.teach()
prof.research()
prof.guide()


# 6. Gadget Store
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Electronics(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

class Accessories(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

class Smartphone(Electronics, Accessories):
    def __init__(self, name, price, brand, warranty, ram, storage):
        Electronics.__init__(self, name, price, brand)
        Accessories.__init__(self, name, price, warranty)
        self.ram = ram
        self.storage = storage

    def display(self):
        print(f"{self.brand} {self.name}, Price: {self.price}, RAM: {self.ram}, Storage: {self.storage}, Warranty: {self.warranty}")

phone = Smartphone("Galaxy S22", 75000, "Samsung", "1 year", "8GB", "128GB")
phone.display()


#Super keyword()
# 7. School Fee Calculation
class Fee:
    def calculate(self):
        print("Base Fee calculated")

class TuitionFee(Fee):
    def calculate(self):
        super().calculate()
        print("Tuition Fee added")

t = TuitionFee()
t.calculate()


# 8. Bank Account
class Account:
    def deposit(self, amount):
        print(f"Deposited {amount} into account")

class SavingsAccount(Account):
    def deposit(self, amount):
        super().deposit(amount)
        print(f"Interest added for deposit of {amount}")

sa = SavingsAccount()
sa.deposit(1000)


# 9. Multiple Levels
class A:
    def show(self):
        print("A show()")

class B(A):
    def show(self):
        super().show()
        print("B show()")

class C(B):
    def show(self):
        super().show()
        print("C show()")

c = C()
c.show()


#MRO(Method Resolution Order)
# 10. Diamond Problem
class A:
    def display(self):
        print("A display()")

class B(A):
    def display(self):
        print("B display()")

class C(A):
    def display(self):
        print("C display()")

class D(B, C):
    pass

d = D()
d.display()  # Follows MRO: D → B → C → A


# 11. Multi-Level + Multiple Inheritance
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.mro())


# 12. Practical Library Example
class Book:
    def info(self):
        print("Book Info")

class EBook(Book):
    def info(self):
        print("EBook Info")

class AudioBook(Book):
    def info(self):
        print("AudioBook Info")

class DigitalLibrary(EBook, AudioBook):
    pass

dl = DigitalLibrary()
dl.info()
print(DigitalLibrary.mro())
