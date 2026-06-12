# Q1
name = input("Enter Name: ")
age = input("Enter Age: ")
city = input("Enter City: ")

print("----- User Information -----")
print("Name:", name)
print("Age:", age)
print("City:", city)


# Q2
age = int(input("Enter Age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# Q3
num = int(input("Enter Number: "))

if num % 2 == 0:
    print(num, "is an Even Number")
else:
    print(num, "is an Odd Number")


# Q4
marks = int(input("Enter Marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")


# Q5
emp_id = input("Enter Employee ID (valid/invalid): ")

if emp_id == "valid":
    wifi = input("Connected to Office WiFi? (yes/no): ")

    if wifi == "yes":
        print("Access Granted")
    else:
        print("Connect to Office WiFi")
else:
    print("Access Denied")


# Q6
marks = int(input("Enter Marks: "))

if marks >= 85:
    income = int(input("Enter Family Income: "))

    if income < 500000:
        print("Scholarship Approved")
    else:
        print("Scholarship Rejected")
else:
    print("Scholarship Rejected")


# Q7
for i in range(1, 21):
    print(i)


# Q8
for i in range(2, 51, 2):
    print(i)


# Q9
num = int(input("Enter Number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# Q10
for i in range(20, 0, -1):
    print(i)


# Q11
i = 1

while i <= 10:
    print(i)
    i += 1


# Q12
i = 10

while i >= 1:
    print(i)
    i -= 1


# Q13
total = 0

for i in range(1, 101):
    total += i

print("Sum =", total)


# Q14
count = 0

for i in range(1, 101):
    if i % 5 == 0:
        count += 1

print("Total Numbers Divisible by 5 =", count)


# Q15
balance = 5000

print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")

choice = int(input("Enter Choice: "))

if choice == 1:
    print("Current Balance:", balance)

elif choice == 2:
    amount = int(input("Enter Amount: "))
    balance += amount
    print("Updated Balance:", balance)

elif choice == 3:
    amount = int(input("Enter Amount: "))

    if amount <= balance:
        balance -= amount
        print("Updated Balance:", balance)
    else:
        print("Insufficient Balance")

else:
    print("Invalid Choice")


# B1
for i in range(1, 101, 2):
    print(i)


# B2
for i in range(1, 21):
    print(i ** 2)


# B3
for i in range(1, 11):
    print(i ** 3)


# B4
for i in range(10, 0, -1):
    print(i)

print(" Blast Off!")


# B5
password = "1234"

for i in range(1, 4):
    user_pass = input("Enter Password: ")

    if user_pass == password:
        print("Login Successful")
        break
    else:
        print("Wrong Password")
else:
    print("Account Locked")