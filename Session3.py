====================================
Codeflex10 - Session 3
====================================

✅ Q1: Accept a list of numbers from user input

nums = list(map(int, input("Enter numbers separated by space: ").split())) print("List:", nums)

------------------------------------------

✅ Q2: Count number of vowels in a sentence

s = input("Enter a sentence: ") vowel = "aeiouAEIOU" count = 0 for ch in s: if ch in vowel: count += 1 print("Vowel count:", count)

------------------------------------------

✅ Q3: Find maximum element from a list without using max()

nums = list(map(int, input("Enter numbers: ").split())) maxi = nums[0] for el in nums: if el > maxi: maxi = el print("Maximum number:", maxi)

------------------------------------------

✅ Q4: Check if a word is palindrome

s = input("Enter a word: ") if s == s[::-1]: print("Palindrome") else: print("Not a palindrome")

------------------------------------------

✅ Q5: Count number of words in a sentence

s = input("Enter a sentence: ") words = s.split() print("Number of words:", len(words))

------------------------------------------

✅ Q6: Find factorial of a number using loop

n = int(input("Enter a number: ")) fact = 1 for i in range(1, n + 1): fact *= i print("Factorial:", fact)

------------------------------------------

✅ Q7: Reverse a list without using reverse() or slicing

nums = list(map(int, input("Enter numbers: ").split())) rev = [] for i in range(len(nums) - 1, -1, -1): rev.append(nums[i]) print("Reversed list:", rev)

------------------------------------------

✅ Q8: Create new list with square of each number

nums = list(map(int, input("Enter numbers: ").split())) squares = [] for n in nums: squares.append(n * n) print("Squared list:", squares)

------------------------------------------

✅ Q9: Check whether a number is prime

num = int(input("Enter a number: ")) if num <= 1: print("Not Prime") else: for i in range(2, int(num**0.5) + 1): if num % i == 0: print("Not Prime") break else: print("Prime")

------------------------------------------

✅ Q10: Print multiplication table of a number

n = int(input("Enter a number: ")) for i in range(1, 11): print(f"{n} * {i} = {n * i}")

====================================