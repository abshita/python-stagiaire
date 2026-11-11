# Python fundamentals for beginners

# 1) Variables and basic data types
name = "Alice"
age = 20
height = 1.75
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} m")
print(f"Student: {is_student}")

# 2) Conditional statements
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 3) For loop
print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(i)

# 4) List and list comprehension
numbers = [1, 2, 3, 4, 5]
even_numbers = [n for n in numbers if n % 2 == 0]
print(f"Even numbers: {even_numbers}")

# 5) Function

def add(a, b):
    return a + b

print(f"10 + 5 = {add(10, 5)}")

# 6) While loop
count = 0
print("Counting with while:")
while count < 3:
    print(count)
    count += 1

# 7) User input
user_name = input("Enter your name: ")
print(f"Welcome, {user_name}!")

# Challenge: Try changing the values and experimenting with the code.
