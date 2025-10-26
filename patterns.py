#right-angle triangle
rows=5
for i in range(1,rows+1):
    print("*" * i)
    
#inverted right-angled triangle
rows=5
for i in range(rows, 0, -1):
    print("*" * i)

#pyramid pattern
rows=5
for i in range(1,rows + 1):
    print(" " * (rows - i) + "*"*i)

#Diamond pattern
rows=5

for i in range(1,rows + 1):
    print(" " * (rows - i)+ "*"*i)
for i in range(1,rows - 1, 0, -1):
    print(" " * (rows-1)+"*"*i )

#number pyramid pattern
rows=5
for i in range(1,rows+1):
    print(" " * (rows-i), end=" ")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#floyd's triangle(number pattern)
n=5
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num += 1
    print()

#pascal's triangle
n=5
for i in range(n):
    num=1
    print(" "*(n - i), end=" ")
    for j in range(i+1):
        print(num,end=" ")
        num=num*(i-j)//(i+j)
    print()

#alphabet pattern(A-E Triangle)
rows=5
for i in range(rows):
    for j in range(i+1):
        print(chr(65+j),end =" ")
        print()

#inverted number pyramid
rows=5
for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(j,end="")
    print()

#Hollow Pyramid (Star Pattern)
rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + i):
        if j == rows - i + 1 or j == rows + i - 1 or i == rows:
            print("*", end="")
        else:
            print(" ", end="")
    print()


#Full Number Pyramid
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()


#Butterfly Pattern
rows = 5
# Upper half
for i in range(1, rows + 1):
    print("*" * i + " " * (2 * (rows - i)) + "*" * i)
# Lower half
for i in range(rows, 0, -1):
    print("*" * i + " " * (2 * (rows - i)) + "*" * i)


#Alphabet Diamond Pattern
rows = 5
for i in range(rows):
    print(" " * (rows - i - 1), end="")
    for j in range(i + 1):
        print(chr(65 + j), end="")
    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end="")
    print()

for i in range(rows - 2, -1, -1):
    print(" " * (rows - i - 1), end="")
    for j in range(i + 1):
        print(chr(65 + j), end="")
    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end="")
    print()

#Hourglass Pattern
rows = 5

# Upper inverted triangle
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "* " * i)
# Lower triangle
for i in range(2, rows + 1):
    print(" " * (rows - i) + "* " * i)


#Numeric Palindrome Triangle
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()






