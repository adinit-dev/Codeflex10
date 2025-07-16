====================================
✅ CodeFlex10 – Session 6 (File Handling Based Practice)
====================================

Q1. Read lines from data.txt and print all lines

with open("data.txt", "r") as f: lines = f.readlines() for line in lines: print(line)

--------------------------------------------------

Q2. Print each word from every line in data.txt

with open("data.txt", "r") as f: lines = f.readlines() for l in lines: words = l.split() print(words)

--------------------------------------------------

Q3. Count how many words in each line start with a vowel

with open("data.txt", "r") as f: lines = f.readlines() for l in lines: words = l.split() newlist = [] for word in words: word2 = word.replace(" ", "").lower() newlist.append(word2) count = 0 vowel = "aeiou" for ch in newlist: if ch[0] in vowel: count += 1 print(count)

--------------------------------------------------

Q4. From words.txt, pick only those starting with uppercase letter and sort them

with open("words.txt", "r") as f: lines = f.readlines() alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" new_list = [] for l in lines: if l[0] in alpha: new_list.append(l.strip()) new_list.sort() print(new_list)

--------------------------------------------------

Q5. From words.txt, print all words that end with a vowel

with open("words.txt", "r") as f: lines = f.readlines() alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" new_list = [] for l in lines: if l[0] in alpha: new_list.append(l.strip()) newlist2 = [] vowel = "aeiouAEIOU" for ch in new_list: if ch[-1] in vowel: newlist2.append(ch) print(newlist2)

--------------------------------------------------

Q6. From numbers.txt, print even numbers

with open("numbers.txt", "r") as f: lines = f.readlines() list2 = [] for line in lines: num = int(line.strip()) list2.append(num) list3 = [] for el in list2: if el % 2 == 0: list3.append(el) print(list3)

--------------------------------------------------

Q7. Print squares of even numbers from numbers.txt

with open("numbers.txt", "r") as f: lines = f.readlines() list2 = [] for line in lines: num = int(line.strip()) list2.append(num) list3 = [] for el in list2: if el % 2 == 0: list3.append(el) list4 = [] for i in list3: sq = i*i list4.append(sq) print(list4)

--------------------------------------------------

Q8. Read numbers from prime.txt and print only prime numbers

with open("prime.txt", "r") as f: lines = f.readlines() list2 = [] for line in lines: num = int(line.strip()) list2.append(num)

for num in list2:
    if num > 1:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            print(num)

--------------------------------------------------

Q9. Read numbers from table.txt and print their multiplication table

def tab_num(n): for i in range(1, 11): print(f"{n} * {i} = {n*i}")

with open("table.txt", "r") as f: lines = f.readlines() list1 = [] for l in lines: list1.append(int(l.strip()))

for el in list1:
    tab_num(el)

--------------------------------------------------

Q10. Write all even numbers from numbers.txt into even.txt file

with open("numbers.txt", "r") as f: lines = f.readlines() evens = [] for line in lines: num = int(line.strip()) if num % 2 == 0: evens.append(str(num))

with open("even.txt", "w") as f: for even in evens: f.write(even + "\n")

====================================