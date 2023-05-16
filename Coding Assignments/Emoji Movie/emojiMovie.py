# 1) Read in the bee_movie_script
with open("Coding Assignments/Emoji Movie/bee_movie_script.txt", "r") as bee_movie:
    b_script = bee_movie.readlines()

# 2) Replace every occurrence of "bee" with "emoii"
e_script = []
for line in b_script:
    if "bee" in line:
        x = line.find("bee")
        line = line[:x] + "emoji" + line[x + 3:]
    
    if "Bee" in line:
        x = line.find("Bee")
        line = line[:x] + "Emoji" + line[x + 3:]
    
    e_script.append(line)


# 3) Write the result to a file
with open("Coding Assignments/Emoji Movie/bee_movie_script.txt", "w") as out_file:
    out_file.writelines(e_script)
