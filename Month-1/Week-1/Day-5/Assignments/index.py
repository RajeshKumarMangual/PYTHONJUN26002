# Q1
full_name = "Rajesh Kumar Mangual"
print(full_name)

# Q2
text = input("Enter a string: ")
print("Length:", len(text))

# Q3
text = input("Enter a string: ")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# Q4
text = "Python Programming"
print(text[:6])
print(text[7:])
print(text[-5:])

# Q5
sentence = input("Enter a sentence: ")
print("Count of 'a':", sentence.count('a'))

# Q6
text = "I love Java Programming"
print(text.replace("Java", "Python"))

# Q7
text = input("Enter a string: ")
print("Reverse:", text[::-1])

# Q8
text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Q9
fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]
print(fruits)

# Q10
numbers = [10, 20, 30]
numbers.append(40)
numbers.insert(1, 15)
print(numbers)

# Q11
colors = ["Red", "Blue", "Green", "Yellow"]
colors.remove("Green")
print(colors)

# Q12
numbers = [10, 50, 20, 80, 30]
print("Largest Number:", max(numbers))

# Q13
numbers = [10, 50, 20, 80, 30]
print("Smallest Number:", min(numbers))

# Q14
numbers = [10, 20, 30, 40, 50]
print("Sum:", sum(numbers))

# Q15
numbers = [10, 15, 20, 25, 30, 35, 40]
for num in numbers:
    if num % 2 == 0:
        print(num)

# Q16
numbers = [10, 20, 30, 40, 50]
count = 0
for i in numbers:
    count += 1
print("Total Elements:", count)

# Q17
cities = ("Delhi", "Mumbai", "Chennai", "Kolkata", "Bangalore")
print(cities)

# Q18
cities = ("Delhi", "Mumbai", "Chennai", "Kolkata", "Bangalore")
print("First Element:", cities[0])
print("Last Element:", cities[-1])

# Q19
numbers = (1, 2, 3, 2, 4, 2, 5)
print("Count of 2:", numbers.count(2))

# Q20
cities = ("Delhi", "Mumbai", "Chennai", "Kolkata", "Bangalore")
city_list = list(cities)
print(city_list)

# Q21
numbers = {1, 2, 3, 4, 5}
print(numbers)

# Q22
numbers = [1, 2, 2, 3, 4, 4, 5, 5]
unique_numbers = set(numbers)
print(unique_numbers)

# Q23
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)

# Q24
numbers = {10, 20, 30}
numbers.add(40)
numbers.remove(20)
print(numbers)

# Q25
student = {
    "name": "John",
    "age": 22,
    "course": "Python",
    "city": "Mumbai"
}
print(student.values())

# Q26
student["age"] = 25
print(student)

# Q27
student["email"] = "john@gmail.com"
print(student)

# Q28
print("Keys:")
for key in student.keys():
    print(key)

print("Values:")
for value in student.values():
    print(value)

# Q29
for key, value in student.items():
    print(key, ":", value)

# Q30
employee = {
    "employee_id": 101,
    "employee_name": "Rajesh",
    "salary": 50000,
    "department": "IT"
}

print("Employee Details")
print("Employee ID:", employee["employee_id"])
print("Employee Name:", employee["employee_name"])
print("Salary:", employee["salary"])
print("Department:", employee["department"])

# Q31
marks = {
    "Math": 85,
    "Science": 90,
    "English": 78
}

total = sum(marks.values())
average = total / len(marks)

print("Total Marks:", total)
print("Average Marks:", average)

# Q32
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Word Count:", len(words))

# Q33
text = "programming"
result = ""

for ch in text:
    if ch not in result:
        result += ch

print(result)

# Q34
keys = ["name", "age", "city"]
values = ["John", 22, "Mumbai"]

data = dict(zip(keys, values))
print(data)

# Q35
students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        student = {"name": name}
        students.append(student)
        print("Student Added")

    elif choice == "2":
        print("Students List:")
        for student in students:
            print(student)

    elif choice == "3":
        search_name = input("Enter Student Name to Search: ")
        found = False

        for student in students:
            if student["name"] == search_name:
                print("Student Found:", student)
                found = True
                break

        if not found:
            print("Student Not Found")

    elif choice == "4":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")