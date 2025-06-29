====================================
✅ CodeFlex10 - Session 4
====================================

Q1. Take 5 numbers input from the user and store them in a list.

numbers = [] for i in range(5): num = int(input("Enter number: ")) numbers.append(num) print(numbers)

------------------------------------------------------------

Q2. Count and print the number of vowels in a sentence.

s = input("Enter sentence: ") vowel = "aeiouAEIOU" count = 0 for ch in s: if ch in vowel: count += 1 print(count)

------------------------------------------------------------

Q3. Take 10 integers input from user and find the maximum without using max().

l = [] for i in range(10): num = int(input("Enter number: ")) l.append(num) print(l) maxi = l[0] for el in l: if el > maxi: maxi = el print("Max:", maxi)

------------------------------------------------------------

Q4. Check if a string is palindrome or not.

s = input("Enter string: ") if s == s[::-1]: print("Palindrome") else: print("Not Palindrome")

------------------------------------------------------------

Q5. Count number of words in a sentence.

s = input("Enter: ") l = s.split() print(len(l))

------------------------------------------------------------

Q6. Find factorial of a number using loop.

n = int(input("Enter number: ")) f = 1 for i in range(1, n+1): f = f * i print("Factorial:", f)

------------------------------------------------------------

Q7. Reverse a list without using reverse() or slicing.

l = [] for i in range(5): l.append(int(input("Enter: "))) rl = [] for i in range(len(l)-1, -1, -1): rl.append(l[i]) print(rl)

------------------------------------------------------------

Q8. Square all even numbers from a file.

with open("numbers.txt", "r") as f: lines = f.readlines() list1 = [] list2 = [] for line in lines: list1 = int(line.strip()) list2.append(list1) print(list2) list3 = [] for el in list2: if el % 2 == 0: list3.append(el) print(list3) list4 = [] for i in list3: sq = i*i list4.append(sq) print(list4)

------------------------------------------------------------

Q9. Check prime numbers from a file and print only primes.

with open("prime.txt", "r") as f: lines = f.readlines() list2 = [] for line in lines: list1 = int(line.strip()) list2.append(list1) print(list2) for n in list2: if n <= 1: continue for i in range(2, int(n**0.5)+1): if n % i == 0: break else: print(n)

------------------------------------------------------------

Q10. Read numbers from file and print multiplication table for each.

def tab_num(n): for i in range(1, 11): print(f"{n} * {i} = {n*i}") with open("table.txt", "r") as f: lines = f.readlines() list1 = [] for l in lines: list1.append(int(l.strip())) for el in list1: tab_num(el)

====================================