====================================
CodeFlex10 - Session 1
====================================

Q1: Take 5 numbers from user and store in list

nums = [] for _ in range(5): nums.append(int(input("Enter a number: "))) print(nums)
------------‐--------------------------------------------------------------

Q2: Count vowels in a string

s = input("Enter a string: ") vowel = "aeiouAEIOU" count = 0 for ch in s: if ch in vowel: count += 1 print("Vowel Count:", count)
------------‐--------------------------------------------------------------

Q3: Find max from a list without using max()

l = list(map(int, input("Enter numbers: ").split())) mx = l[0] for el in l: if el > mx: mx = el print("Max:", mx)
------------‐--------------------------------------------------------------
	

Q4: Check if string is palindrome

s = input("Enter a string: ") if s == s[::-1]: print("Palindrome") else: print("Not Palindrome")
------------‐--------------------------------------------------------------


Q5: Count words in sentence

s = input("Enter a sentence: ") print("Word count:", len(s.split()))
------------‐--------------------------------------------------------------


Q6: Factorial using loop

n = int(input("Enter a number: ")) fact = 1 for i in range(1, n + 1): fact *= i print("Factorial:", fact)
------------‐--------------------------------------------------------------


Q7: Reverse list without using reverse()

l = list(map(int, input("Enter list: ").split())) rl = [] for i in range(len(l) - 1, -1, -1): rl.append(l[i]) print(rl)
------------‐--------------------------------------------------------------


Q8: Square each element in list

l = list(map(int, input("Enter list: ").split())) sq = [] for el in l: sq.append(el ** 2) print(sq)
------------‐--------------------------------------------------------------


Q9: Check if number is prime

n = int(input("Enter number: ")) if n <= 1: print("Not Prime") else: for i in range(2, int(n**0.5) + 1): if n % i == 0: print("Not Prime") break else: print("Prime")
------------‐--------------------------------------------------------------
	

Q10: Multiplication table

n = int(input("Enter number: ")) for i in range(1, 11): print(f"{n} * {i} = {n*i}")

====================================

		