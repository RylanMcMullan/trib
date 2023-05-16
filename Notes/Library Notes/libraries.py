num = random.random()
print(num)

# Python3 program to demonstrate the use of
# choice() method

# import random
import random # https://docs.python.org/3/library/random.html?highlight=random#module-random

# prints a random value from the list
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))

# prints a random item from the string
string = "striver"
print(random.choice(string))


# Python code to demonstrate the working of
# choice() and randrange()

# importing "random" for random operations
import random

# using choice() to generate a random number from a
# given list of numbers.
print("A random number from list is : ", end="")
print(random.choice([1, 4, 8, 10, 3]))

# using randrange() to generate in range from 20
# to 50. The last parameter 3 is step size to skip
# three numbers when selecting.
print("A random number from range is : ", end="")
print(random.randrange(20, 50, 3))


# import the random module
import random


# declare a list
sample_list = ['A', 'B', 'C', 'D', 'E']

print("Original list : ")
print(sample_list)

# first shuffle
random.shuffle(sample_list)
print("\nAfter the first shuffle : ")
print(sample_list)

# second shuffle
random.shuffle(sample_list)
print("\nAfter the second shuffle : ")
print(sample_list)
