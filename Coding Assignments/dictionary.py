Teams = {
    "Penn State": {
        "Team Name": "Penn State",
        "Head Coach": "Micah Shrewsberry",
        "Conference": "B10, 10th Place",
        "Roster": ["Jalen Pickett", "Seth Lundy", "Camren Wynter", "Andrew Funk", "Kebba Njie"],
        "Leading Scorers": ["Pickett 17.9", "Lundy: 14.4", "Funk: 12.1"],
        "Seed/Region": ("10-seed", "Big Ten"),
        "Ratings": ["KenPom: 40th", "Net: 48th"],
        "Predictions": "71 to 69, loss"
    },
    "Maryland": {
        "team name": "Maryland",
        #coach :)
        "head coach":"Kevind Willard",
        "conference":"Big Ten, 8th",
        "roster": ["J. Young", "H.Hart", "D. Scott", "J.Reese", "D. Carey"],
        "leading scorers": ["Young", "Hart", "Scott"],
        "seed/region": ("8th seed", "South Region"),
        "ratings": ["kenPom: 20th", "net: 31"],
        "predictions": "70 to 66, loss"
    },
    "Illinois": {
        "Team Name": "Illinois",
        "Head Coach": "Brad UnderWood",
        "Conference": "Big Ten, 5th Place",
        "Roster": ["TERRENCE SHANNON JR.", "CONNOR SERVEN", "AYDEN EPPS", "AJ REDD", "LUKE GOODE"],
        "Leading Scorers": ["Terrence: 17.1", "", "Matthew: 12.8"],
        "Seed/Region": ("9-seed", "West Region"),
        "Ratings": ["KenPom: 33rd", "Net: 34th"],
        "Predictions": "71 to 68, win"
    },
    "Purdue": {
        "Team Name": "Purdue",
        "Head Coach": "Matt Painter",
        "Conference": "Big 10 1st place",
        "Roster": ["Zach Edey", "Braden Smith", "Fletcher Loyer", "Caleb Furst", "Mason Gillis"],
        "Scoring Leaders": ["Edey: 22.3", "Loyer: 10.9", "Smith: 9.8"],
        "Seed/Region": ("1-seed", "East Region"),
        "Ratings": ["KenPom 6th", "Net: 3rd"],
        "Prediction": "82 to 56, win"
    },
}

while True:
    print("\n")
    ask = input("What team do you want to look up? ") # ask for a team
    ask1 = input("What do you want to look up? ") # ask for information about it
    for i in Teams:
        if i.lower() == ask.lower(): # check if ask is in the dictionary
            for j in Teams[i]:
                if j.lower() == ask1.lower(): # check if ask1 is in the team dictionary
                    print(Teams[i][j]) # print the information
    print("\n")
    off = input("Do you want to look something else up? (y/n) ")
    if off.lower() == "n":
        break
    else:
        continue