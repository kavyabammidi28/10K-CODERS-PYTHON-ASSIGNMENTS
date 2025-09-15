# 1. Class for Books
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

# Creating two objects of Book
book1 = Book("Harry Potter", "J.K. Rowling", 350)
book2 = Book("The Alchemist", "Paulo Coelho", 200)


# 2. Class for Cars
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

# Creating two objects of Car
car1 = Car("Tesla", "Model S", 2023)
car2 = Car("BMW", "X5", 2022)


# 3. Class for Gadgets
class Gadget:
    def __init__(self, name, company, price):
        self.name = name
        self.company = company
        self.price = price

# Creating two objects of Gadget
gadget1 = Gadget("Smartphone", "Apple", 80000)
gadget2 = Gadget("Laptop", "Dell", 60000)


# 4. Class for Movies
class Movie:
    def __init__(self, name, director, rating):
        self.name = name
        self.director = director
        self.rating = rating

# Creating two objects of Movie
movie1 = Movie("Inception", "Christopher Nolan", 9.0)
movie2 = Movie("Avatar", "James Cameron", 8.5)


# Printing some details
print("Book 1:", book1.title, "by", book1.author)
print("Car 1:", car1.brand, car1.model, "-", car1.year)
print("Gadget 1:", gadget1.name, "from", gadget1.company, "price:", gadget1.price)
print("Movie 1:", movie1.name, "directed by", movie1.director, "rating:", movie1.rating)
