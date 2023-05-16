dumb_word = ""
for letter in "supercalifragilisticexpialidocious":
    if letter > "m":
      continue
    dumb_word += letter
    print(dumb_word)

name = input("What is your name? ")
print(name)
#print(type(name))

age = input("What is your age? ")
print(age)
"""
print(type(age))
"""

print("3" * 3)
print(type(3/3))
print(4 ** 3)