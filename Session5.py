====================================
# CodeFlex10 – Session 5
====================================

# Q1. Check if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
-----------‐--------------------------------------------------------------


# Q2. Count how many times a character appears in a string
s = input("Enter a string: ")
ch = input("Enter a character to count: ")
print("Count:", s.count(ch))
------------‐--------------------------------------------------------------


# Q3. Print all numbers from 1 to n that are divisible by both 3 and 5
n = int(input("Enter a number: "))
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=' ')
 ------------‐--------------------------------------------------------------


# Q4. Calculate the sum of digits of a number
n = int(input("\nEnter a number: "))
sum_digits = 0
while n > 0:
    sum_digits += n % 10
    n //= 10
print("Sum of digits:", sum_digits)
------------‐--------------------------------------------------------------


# Q5. Replace all spaces in a string with hyphens
s = input("Enter a sentence: ")
print("Modified:", s.replace(" ", "-"))
------------‐--------------------------------------------------------------


# Q6. Find the second largest number in a list
lst = list(map(int, input("Enter list elements: ").split()))
lst = list(set(lst))
lst.sort()
print("Second largest:", lst[-2])
------------‐--------------------------------------------------------------


# Q7. Print factorial of a number using while loop
n = int(input("Enter a number: "))
fact = 1
while n > 0:
    fact *= n
    n -= 1
print("Factorial:", fact)
------------‐--------------------------------------------------------------


# Q8. Count total vowels in a string
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for c in s if c in vowels)
print("Vowel count:", count)
------------‐--------------------------------------------------------------


# Q9. Find the smallest number in a list without using min()
lst = list(map(int, input("Enter list: ").split()))
small = lst[0]
for num in lst:
    if num < small:
        small = num
print("Smallest number:", small)
------------‐--------------------------------------------------------------


# Q10. Print multiplication table of a number up to 10
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
    ====================================