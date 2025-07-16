====================================
✅ CodeFlex10 – Session 7
====================================
Topic: Object-Oriented Programming – Beginner Level

---------------------------------------------

Q1. Create a Student class with name and roll number. Display the student's details.

class Student: def init(self, name, roll_num): self.name = name self.roll_num = roll_num

def display(self):
    print("Name : ", self.name)
    print("Roll num : ", self.roll_num)

n1 = Student("Aditya", 123) n1.display()

---------------------------------------------

Q2. Create a Rectangle class. Calculate and display area and perimeter.

class Rectangle: def init(self, length, breadth): self.length = length self.breadth = breadth

def area(self):
    print("area : ", self.length * self.breadth)

def perimeter(self):
    print("perimeter :", 2 * (self.length + self.breadth))

r1 = Rectangle(3, 7) r1.area() r1.perimeter()

---------------------------------------------

Q3. Create a Circle class. Calculate and display area and circumference.

class Circle: def init(self, radius): self.radius = radius

def area(self):
    print("Area :", 3.14 * self.radius * self.radius)

def circumference(self):
    print("Circumference :", 2 * 3.14 * self.radius)

r1 = Circle(5) r1.area() r1.circumference()

---------------------------------------------

Q4. Create an Employee class. Display name and salary.

class Employee: def init(self, name, salary): self.name = name self.salary = salary

def display(self):
    print("Name :", self.name)
    print("Salary :", self.salary)

e1 = Employee("Roshan", 55000) e1.display()

---------------------------------------------

Q5. Create a BankAccount class. Handle deposit, withdrawal, and display balance.

class BankAccount: def init(self, name, balance): self.name = name self.balance = balance

def deposit(self, amount):
    self.balance += amount

def withdraw(self, amount):
    if self.balance >= amount:
        self.balance -= amount
    else:
        print("Insufficient balance")

def display(self):
    print("Balance :", self.balance)

b1 = BankAccount("Aditya", 10000) b1.deposit(5000) b1.withdraw(12000) b1.display()

---------------------------------------------

Q6. Create a Book class. Apply 10% discount and display final price.

class Book: def init(self, name, author, price): self.name = name self.author = author self.price = price

def discount(self):
    final_price = self.price - (self.price / 10)
    print("Final price :", final_price)

def display(self):
    print("Name :", self.name)
    print("Author :", self.author)
    print("Price :", self.price)

b1 = Book("Atomic Habits", "James Clear", 500) b1.discount() b1.display()

---------------------------------------------

Q7. Create StudentMark class. Store 3 marks and calculate average.

class StudentMark: def init(self, name, marks): self.name = name self.marks = marks

def average(self):
    avg = sum(self.marks) / len(self.marks)
    return avg

def display(self):
    print("Name :", self.name)
    print("Avg Mark :", self.average())

s1 = StudentMark("Adi", [45, 76, 89]) s1.display()

---------------------------------------------

Q8. Create Laptop class. Apply discount and display discounted price.

class Laptop: def init(self, brand, model, price): self.brand = brand self.model = model self.price = price

def apply_discount(self, percentage):
    self.price = self.price - (self.price * percentage / 100)

def display(self):
    print("Brand Name :", self.brand)
    print("Model Name :", self.model)
    print("Discounted Price :", self.price)

l1 = Laptop("Apple", "M5", 100000) l1.apply_discount(15) l1.display()

---------------------------------------------

Q9. Create Movie class. Check if classic (before 2000).

class Movie: def init(self, title, director, year): self.title = title self.director = director self.year = year

def is_classic(self):
    return self.year < 2000

def display(self):
    print("Movie Title :", self.title)
    print("Director :", self.director)
    print("Year :", self.year)

m1 = Movie("Oppenheimer", "Nolan", 2024) if m1.is_classic(): print("Classic Movie") else: print("Non Classic Movie") m1.display()

---------------------------------------------

Q10. Create Car class. Check if the car is old (before 2015).

class Car: def init(self, brand, model, year): self.brand = brand self.model = model self.year = year

def is_old(self):
    return self.year < 2015

def display(self):
    print("Brand :", self.brand)
    print("Model :", self.model)
    print("Year :", self.year)

c1 = Car("BMW", "B1", 2011) if c1.is_old(): print("Old Car") else: print("New Car") c1.display()

====================================