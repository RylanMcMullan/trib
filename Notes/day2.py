print("Example 1")
x = 5
y = 12
print(x > y)
print(y <= x)
print(x != 2 + 3)
print(y == 17 - x)
print("happy" == "sad")
print("happy" != "sad")
print("happy" < "sad")

print("\nExample 2")
tr = True
f = False

print(f or tr)
print(f and tr)

not(tr and f) # means not either

print("\nExample 3")
x = 5
y = 12

if x < 2:
    print("monty")
elif y <= 8:
    print("python")
else:
    print("flying circus")

print("\nExample 4") # If it is a weekday and you are too young to work, you should go to school
dow = bool(input("is it a weekday? "))
if dow == True:
    age = int(input("What is your age? "))
    if age > 4 and age < 19: # This is not a mistake i just support child labor
        print("You should be at school")
    else:
        print("You should be at work.")
else:
    print("You have the day off!")



