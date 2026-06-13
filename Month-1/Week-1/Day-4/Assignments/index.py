# Q1
def welcome_user(name):
    print(f"Welcome, {name}!")

welcome_user(input("enter your name:"))


# Q2
def check_even_odd(num):
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

check_even_odd(10)


# Q3
def largest_number(a, b):
    if a > b:
        print(f"{a} is greater")
    else:
        print(f"{b} is greater")

largest_number(10, 20)


# Q4
def check_voting(age):
    if age >= 18:
        print("Eligible")
    else:
        print("Not Eligible")

check_voting(20)


# Q5
def calculate_discount(price):
    if price > 5000:
        discount = price * 0.10
    else:
        discount = 0
    print("Discount Amount =", discount)

calculate_discount(6000)


# Q6
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(5)


# Q7
def print_even_numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)

print_even_numbers(10)


# Q8
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

multiplication_table(5)


# Q9
def countdown(n):
    while n > 0:
        print(n)
        n -= 1

countdown(5)


# Q10
def sum_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_numbers(5))


# Q11
def find_square(n):
    return n * n

print(find_square(7))


# Q12
def count_positive(nums):
    count = 0
    for i in nums:
        if i > 0:
            count += 1
    print(count, "Positive Numbers")

count_positive([1, -2, 3, -4, 5])


# Q13
def student_result(marks):
    if marks >= 90:
        print("Grade A")
    elif marks >= 70:
        print("Grade B")
    elif marks >= 40:
        print("Grade C")
    else:
        print("Fail")

student_result(85)


# Q14
def print_odd_numbers(n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i)

print_odd_numbers(10)


# Q15
def login_verification(username, password):
    if username == "admin":
        if password == "1234":
            print("Login Successful")
        else:
            print("Wrong Password")
    else:
        print("Invalid User")

login_verification("admin", "1234")


# Bonus 1
def factorial_calculator(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial_calculator(5))


# Bonus 2
def reverse_number(num):
    return int(str(num)[::-1])

print(reverse_number(1234))


# Bonus 3
def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count

print(count_vowels("Python"))


# Bonus 4
def guessing_checker(guess):
    secret_number = 7
    if guess == secret_number:
        print("Correct Guess")
    else:
        print("Try Again")

guessing_checker(7)


# Bonus 5
def pattern_printing(n):
    for i in range(1, n + 1):
        print("*" * i)

pattern_printing(5)


# Challenge Question
def employee_bonus(name, salary, experience):
    if experience >= 5 and salary < 50000:
        bonus = salary * 0.20
    elif experience >= 3:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.05

    final_salary = salary + bonus

    print("Employee Name:", name)
    print("Salary:", salary)
    print("Bonus Amount:", bonus)
    print("Final Salary:", final_salary)

employee_bonus("Rajesh", 45000, 6)