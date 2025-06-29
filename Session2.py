====================================
Codeflex10 -Session 2
====================================

# Question 1: Accept list from user
nums = list(map(int, input("Enter numbers: ").split()))
print(nums)

------------‐--------------------------------------------------------------

# Question 2: Count vowels
s = input("Enter a string: ")
vowel = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowel:
        count += 1
print(count)

------------‐--------------------------------------------------------------

# Question 3: Find max (no max())
n = list(map(int, input().split()))
m = n[0]
for i in n:
    if i > m:
        m = i
print(m)

------------‐--------------------------------------------------------------

# Question 4: Palindrome
s = input()
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
  
-------------‐--------------------------------------------------------------


# Question 5: Word count
s = input()
w = s.split()
print(len(w))
------------‐--------------------------------------------------------------


# Question 6: Factorial
n = int(input())
f = 1
for i in range(1, n+1):
    f *= i
print(f)
------------‐--------------------------------------------------------------


# Question 7: Reverse list (no slicing)
l = list(map(int, input().split()))
r = []
for i in l:
    r = [i] + r
print(r)

------------‐--------------------------------------------------------------

# Question 8: Square list
l = list(map(int, input().split()))
sq = []
for i in l:
    sq.append(i*i)
print(sq)
------------‐--------------------------------------------------------------


# Question 9: Prime
n = int(input())
if n <= 1:
    print("Not Prime")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
------------‐--------------------------------------------------------------


# Question 10: Table
n = int(input())
for i in range(1, 11):
    print(f"{n} * {i} = {n*i}")
    
====================================