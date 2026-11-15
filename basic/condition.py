# Condition example

age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

score = 75

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
else:
    print("Need more practice")

# Boolean values: True means true, False means false
is_student = True
has_finished_homework = False
print("Is student:", is_student)
print("Has finished homework:", has_finished_homework)

# and: both conditions must be true
if age >= 18 and is_student:
    print("You are an adult student.")

# or: at least one condition must be true
has_ticket = False
is_on_guest_list = True
if has_ticket or is_on_guest_list:
    print("You can enter.")

# not: reverses a boolean value
if not has_finished_homework:
    print("Finish your homework.")

# and is evaluated before or: (a > 2 and b < 1) or c == 3
a = 4
b = 3
c = 3

if a > 2 and b < 1 or c == 3:
    print("A")
else:
    print("B")

# Truth table: and is True only when both values are True
print("\nAND:")
print("True and True =", True and True)
print("True and False =", True and False)
print("False and True =", False and True)
print("False and False =", False and False)

# Truth table: or is True when at least one value is True
print("\nOR:")
print("True or True =", True or True)
print("True or False =", True or False)
print("False or True =", False or True)
print("False or False =", False or False)

# not reverses the value
print("\nNOT:")
print("not True =", not True)
print("not False =", not False)
