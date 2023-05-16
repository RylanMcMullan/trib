#information about the previous batman trilogy

batman_begins = {
    "title":"Batman Begins",
    "year":2005,
    "cast":["Christian Bale","Michael Caine","Liam Neeson","Katie Holmes"],
    "genres":["Superhero"]
}

dark_knight = {
     "title":"The Dark Knight",
     "year":2008,
     "cast":["Christian Bale","Michael Caine","Heath Ledger","Gary Oldman"],
     "genres":["Superhero"]
}

dark_knight_rises = {
     "title":"The Dark Knight Rises",
     "year":2012,
     "cast":["Christian Bale","Michael Caine","Gary Oldman","Tom Hardy"],
     "genres":["Crime","Drama","Superhero"]
}

print(dark_knight['cast'] [2])
print(batman_begins['title'])
print(dark_knight['year'])
print(dark_knight_rises['cast'])
print(dark_knight_rises['genres'] [1])

dark_knight['year'] = [2023]
dark_knight_rises['cast'].append("Braden_Tribolet")

print(dark_knight['year'])
print(dark_knight_rises['cast'])

batman_begins['Characters'] = ['Batman', 'Alfred', "Scarecrow"]
dark_knight['Characters'] = ['Batman', 'Alfred', "Joker"]
dark_knight_rises['Characters'] = ['Batman', 'Alfred', "Bane"]

print(batman_begins['Characters'] [2])

print('title' in  dark_knight)