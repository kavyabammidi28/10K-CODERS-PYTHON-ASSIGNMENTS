#1. Squares of odd numbers
squares_of_odds = [n**2 for n in range(1, 21) if n % 2 != 0]
print(squares_of_odds)

#2. Cube dictionary
cube_dict = {n: n**3 for n in range(1, 11)}
print(cube_dict)


#3. Set of vowels
vowels = {ch for ch in "programming in python" if ch in "aeiou"}
print(vowels)


#4. Reverse dictionary
d = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = {v: k for k, v in d.items()}
print(reversed_dict)


#5. Multiplication table (list of tuples)
table = [(n, n*2, n*3) for n in range(1, 6)]
print(table)


#6. Filter positive numbers
nums = [-3, -1, 0, 2, 4, -6]
positives = [n for n in nums if n > 0]
print(positives)


#7. Word lengths
sentence = "Python makes coding easier"
word_lengths = {word: len(word) for word in sentence.split()}
print(word_lengths)


#Even or Odd Labeling
labels = ["Even" if n % 2 == 0 else "Odd" for n in range(1, 11)]
print(labels)

#Squares as Tuples
squares_tuple = tuple(n**2 for n in range(1, 8))
print(squares_tuple)

#Remove Duplicates
nums = [1,2,2,3,4,4,5,5,6]
unique_sorted = sorted({n for n in nums})
print(unique_sorted)


#1.Right Aligned Triangle
n = 5
for i in range(1, n+1):
    print("  " * (n-i) + "* " * i)


#2.Right Angle Inverted Triangle
n = 5
for i in range(n, 0, -1):
    print("  " * (n-i) + "* " * i)


#3.Number Square Pattern(5x5)
n = 5
for i in range(1, n+1):
    print((str(i) + " ") * n)


#4.Incresing Number Triangle
n = 5
for i in range(1, n+1):
    print(" ".join(str(j) for j in range(1, i+1)))


#5.Decreasing Number Triangle
n = 5
for i in range(n, 0, -1):
    print(" ".join(str(j) for j in range(1, i+1)))


#6.Hollow Square
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


#7.Recatangle of Numbers(3x6)
rows, cols = 3, 6
for i in range(rows):
    print(" ".join(str(j) for j in range(1, cols+1)))


#8.Pyramid Pattern
n = 5
for i in range(1, n+1):
    print(" " * (n-i) + "* " * i)


#9.Inverted Pyramid
n = 5
for i in range(n, 0, -1):
    print(" " * (n-i) + "* " * i)


#10.Diamond Pattern
n = 5
# Upper part
for i in range(1, n+1):
    print(" " * (n-i) + "* " * i)
# Lower part
for i in range(n-1, 0, -1):
    print(" " * (n-i) + "* " * i)

