def add(x, y = 5):
    print(x + y)
add(10)

age = int(input("What is your age? "))
print(f"Your age is {age}")

try:
    age = int(input("What is your age? "))
    print(f"Your age is {age}")
except ValueError:
    print("That is not an integer")

x = 3
y = 0

try:
    print(x/y)
except ZeroDivisionError:
    print("Can't divide by zero")