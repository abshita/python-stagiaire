# Try/except example

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
finally:
    print("This code always runs.")
