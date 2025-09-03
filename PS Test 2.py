'''#1. print numbers
for i in range(1,101):
    if (i%3 == 0 or i%5 == 0) and not (i%3 == 0 and i%5 == 0):
        print(i, end=" ")'''

#2.Second largest number
nums = [10, 28, 22, 38, 50]

first = second = float('-inf')   
for n in nums:
    if n > first:                
        second = first           
        first = n                
    elif n > second and n != first:  
        second = n
print("Second largest:", second)


#3. palindrome
def is_palindrome(n):
    if len(n) <= 1:
        return True
    if n[0] != n[-1]:
        return False
    return is_palindrome(n[1:-1])

print(is_palindrome('level'))


#4.pyramid
def pyramid(n):
    for i in range(1,n+1):
        print(' ' * (n-1),end=' ')
        print("*" * i)
pyramid(5)

#5.gcd of two no.s
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(56, 98))   

#6.list of prime numbers
nums = [10, 15, 2, 3, 7, 9, 11, 20]

primes = [n for n in nums if primes(n)]
print("Prime numbers:", primes)


#7.count the words 
def word_frequency(sentence):
    words = sentence.split()   
    freq = {}                  
    
    for word in words:
        if word in freq:
            freq[word] += 1    
        else:
            freq[word] = 1     
    
    return freq

text = "python is easy and python is powerful"
print(word_frequency(text))

#8. print prime numbers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

#9.
def find_pairs(nums, target):
    pairs = []
    n = len(nums)

    for i in range(n):
        for j in range(i+1, n):   
            if nums[i] + nums[j] == target:
                pairs.append((nums[i], nums[j]))
    
    return pairs

nums = [2, 4, 3, 7, 5, 8, -1]
target = 7
print("Pairs:", find_pairs(nums, target))


#10. armstrong number
def is_armstrong(num):
    digits = str(num)
    power = len(digits)  
    
    total = sum(int(d)**power for d in digits)
    if total == num:
        print(num, "is an Armstrong number")
    else:
        print(num, "is NOT an Armstrong number")

is_armstrong(153) 





