# lists and tuples store data 
# tuples are immutable

teams = ["Colts", "Patriots", "Bears"]
print(teams)

# append (add to the end of the list)
teams.append("Steelers")
print(teams)

# insert (add element to specific index)
teams = ["Colts", "Patriots", "Bears"]

teams.insert(1, "Steelers")
print(teams)

# delete (delete a specific index)
teams = ["Colts", "Patriots", "Bears"]

del teams[-1]
print(teams)

# remove (remove specif element)
teams = ["Colts", "Patriots", "Bears"]

teams.remove("Patriots")
print(teams)

# pop (take last element out)
teams = ["Colts", "Patriots", "Bears"]

teams.pop()
first_team = teams.pop(0)
print(teams)
print(first_team)

teams = ["Colts", "Patriots", "Bears"]
string_teams = "Ravens Cowboys Falcons"

# split (separate parts of a string)
print(string_teams.split(" "))

# join (combine parts of string in list)
print(" ".join(teams))

teams = ["Colts", "Patriots", "Bears"]
string_teams = "Ravens Cowboys Falcons"

teams2 = (string_teams.spilt(' '))

# extend (add two lists together)
teams.extend(teams2)
print(teams)

# reverse (reverse each item in a list)
teams.reverse()
print(teams)

# sort (put in alphabetical order)
teams.sort()
print(teams)

# count (count a specific element in list)
print(teams.count("colts"))


for i in teams:
    print(f"My favorite team is the {i}.")

teams = ["Colts", "Bears", "Chiefs"]

auth = ("Martin", "Luther", "King, Jr.")

def citation(author_name):
    return f"{author_name[-1]}, {' '.join(author_name[0:1])}"
    
print(citation(auth))