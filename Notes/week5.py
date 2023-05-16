s = "One ring to rule them all"

print(s)
print(s[0])
print(s[10])
print(len(s))
print(s[5])
print(s[-1])

print(s[5:10])
print(s[0:6])
print(s[-23:-19])
print(s[5:])
print(s[:5])
print(s[:20])

s = "hello"
#s[0] = "j"
s = "jello"
print(s)

def Modify_string(wrd, ltr):
    wrd2 = f"{ltr + wrd[1:]}"
    return wrd2

print(Modify_string("bat", "h"))

from string import ascii_lowercase as a_low
print(a_low)

from string import ascii_lowercase as a_low
text = "Bee MoVie"
print(text.lower())
if "e" in a_low:
    print("e is in the alphabet")

# challenge

# count letters in alphabet
string = input("Give me a string: ")
def count(str):
    x = 0
    for i in str.lower():
        if i in a_low:
            x = x + 1
    print(f"{x} letters in string")
count(string)

# count e's in string
string = input("Give me a string: ")
def count_e(str):
    x = 0
    for i in str.lower():
        if i == "e":
            x = x + 1
    print(f"{x} e's in string")
count_e(string)


