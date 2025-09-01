#1.Square of a Number
square = lambda x: x**2
print(square(5))   # 25

#2.Check Even or ODD
is_even = lambda x: x % 2 == 0
print(is_even(4))   # True
print(is_even(5))   # False

#3.Find Maximum of Two Numbers
max_num = lambda a, b: a if a > b else b
print(max_num(10, 20))   # 20

#4.ADD Two Numbers
add = lambda a, b: a + b
print(add(4, 6))   # 10

#5.Sort a list of Tuples
data = [(1, 5), (2, 3), (4, 1)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)   # [(4, 1), (2, 3), (1, 5)]

#6.Filter Even Numbers
nums = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)   # [2, 4, 6, 8, 10]

#7.Map with Lambda
nums = [1, 2, 3, 4, 5]
cubes = list(map(lambda x: x**3, nums))
print(cubes)   # [1, 8, 27, 64, 125]


#8.Reduce with Lambda
from functools import reduce

nums = [2, 3, 4, 5]
product = reduce(lambda a, b: a*b, nums)
print(product)   # 120


#9.Sort by Name Length
words = ["apple", "banana", "kiwi", "grapes"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)   # ['kiwi', 'apple', 'grapes', 'banana']

#10.Find Palindromes
words = ["madam", "python", "level", "world"]
palindromes = list(filter(lambda w: w == w[::-1], words))
print(palindromes)   # ['madam', 'level']

#11.Custom Sorting
words = ["Cat", "apple", "Banana", "dog"]
sorted_case = sorted(words, key=lambda x: x.lower())
print(sorted_case)   # ['apple', 'Banana', 'Cat', 'dog']

#12.Conditional Lambda
check_num = lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Zero")
print(check_num(10))   # Positive
print(check_num(-3))   # Negative
print(check_num(0))    # Zero

#15.Dictionary Sorting by Values
data = {'a': 3, 'b': 1, 'c': 2}
sorted_items = sorted(data.items(), key=lambda x: x[1])
print(sorted_items)   # [('b', 1), ('c', 2), ('a', 3)]
