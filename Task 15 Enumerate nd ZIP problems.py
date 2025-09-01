#TASKS ON ENUMERATE
#Simple Index Printing
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

#Start Index From 1
students = ["Alice", "Bob", "Charlie"]

for index, student in enumerate(students, start=1):
    print(index, student)

#Replace for with enumerate
colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(index, color)


#Find Index Of a Specific Value
languages = ["java", "c++", "python", "ruby"]

for index, lang in enumerate(languages):
    if lang == "python":
        print("Index of python:", index)


#Enumerate on a string
languages = ["java", "c++", "python", "ruby"]

for index, lang in enumerate(languages):
    if lang == "python":
        print("Index of python:", index)


#ZIP PROBLEMS
#Combine two Lists
names = ["Alice", "Bob", "Charlie"]
marks = [85, 90, 78]

paired = list(zip(names, marks))
print(paired)


#Iterate with ZIP
for name, mark in zip(names, marks):
    print(f"{name} scored {mark}")


#Unzipping
pairs = [("a", 1), ("b", 2), ("c", 3)]

keys, values = zip(*pairs)
print("Keys:", keys)
print("Values:", values)

