import random

# 1. Generate a random float between 0.0 and 1.0
rand_float = random.random()
print("Random Float:", rand_float)

# 2. Generate a random integer between 1 and 100
rand_int = random.randint(1, 100)
print("Random Integer (1-100):", rand_int)

# 3. Pick a random fruit from a list
fruits = ["apple", "banana", "mango", "orange"]
rand_fruit = random.choice(fruits)
print("Random Fruit:", rand_fruit)

# 4. Shuffle a list of numbers
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled List:", numbers)

# 5. Generate 5 random integers between 10 and 50
rand_integers = [random.randint(10, 50) for _ in range(5)]
print("5 Random Integers (10-50):", rand_integers)
