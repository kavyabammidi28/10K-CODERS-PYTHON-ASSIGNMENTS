# Reverse a string without built-in function
text = "Python"
reverse_text = ""

for char in text:
    reverse_text = char + reverse_text   # Add character in front

print("Original String:", text)
print("Reversed String:", reverse_text)

# Marks of 5 students
marks = [400, 450, 530, 550, 570]

total = 0
for m in marks:
    total += m

average = total / len(marks)

print("Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)


# Given sides
a, b, c = 5, 5, 5

if (a + b > c) and (a + c > b) and (b + c > a):
    print("The sides form a Triangle")
else:
    print("The sides do NOT form a Triangle")
