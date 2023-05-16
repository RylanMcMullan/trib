str = {}

def vowel(str):
    if (((int(str).startswith("a") or str.startswith("e")) or (str.startswith("i") or str.startswith("o"))) or (str.startswith("u"))):
        str = "an ${str}"
    else:
        str = "a ${str}"

print("Welcome to MadLibs")
noun1 = input("Give me a noun! ")
verb1 = input("Give me a verb! ")
adj1 = input("Give me an adjective! ")
noun2 = input("Give me another noun! ")
verb2 = input("Give me another verb! ")
loc1 = input("Give me a location ")
adj2 = input("Give me another adjective! ")
noun3 = input("Give me another noun! ")
noun4 = input("Give me another noun! ")

print(f"I took my {noun1} for {vowel(verb1)}.")
print(f"Then I asked my {adj1} {noun2} if I could {verb2} to {loc1}.")
print(f"Once I arrived at {loc1}, I saw {vowel(adj2)} {noun3}.")
print(f"The {adj2} {noun3} asked me what I was doing there.")
print(f"I told the {adj2} {noun3} I'm looking for {vowel(noun4)}.")