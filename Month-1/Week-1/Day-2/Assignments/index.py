a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
#Task 1
print("Sum =", a + b)
#Task 2
print("Subtraction =", a - b)
#Task 3
print("Multiplication =", a * b)
#Task 4
print("Division =", a / b)
#Task 5
print("Remainder =", a % b)
#Task 6
print("Floor Division =", a // b)
#Task 7
print("Power =", a ** b)
#Task 8
print("Equal:", a == b)
#Task 9
print("Not Equal:", a != b)
#Task 10
print("Greater Than:", a > b)
#Task 11
print("Less Than:", a < b)
#Task 12
print("Greater Than or Equal:", a >= b)
#Task 13
print("Less Than or Equal:", a <= b)
#Task 14
age = int(input("Enter age: "))
citizen = input("Are you a citizen? (yes/no): ")
print("Eligible for Vote:", age >= 18 and citizen == "yes")
#Task 15
student = input("Are you a student? (yes/no): ")
premium = input("Do you have premium membership? (yes/no): ")
print("Eligible for Discount:",student== "yes" or premium == "yes")
#Task 16
experience = int(input("Enter years of experience: "))
rating = int(input("Enter performance rating: "))
print("Eligible for Bonus:",experience >= 5 and rating >= 8)
#Task 17
marks = int(input("Enter marks: "))
sports = input("Sports quota? (yes/no): ")
print("Eligible for Scholarship:",marks >= 80 or sports == "yes")
#Task 18
num = int(input("Enter a number: "))
print("Between 1 and 100:", 1 <= num <= 100)
#Task 19
num = int(input("Enter a number: "))
print("Even:", num % 2 == 0)
print("Odd:", num % 2 != 0)
# Task 20
value = bool(input("Enter True or False: "))
bool_value = value == "true"
print("Opposite Value:", not bool_value)