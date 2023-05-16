default_str = "We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness."

    # amount functions
def wrdct(str): # of words fn
    x = 1 # of words default (assuming first word in string exists)
    for i in str.lower(): # looping throught the string
        if i == " ": # check if there is a space between letters
            x = x + 1 # add to x for every space in string
    return x
    #print(f"{x} words in string")

def charct(str): # of letters fn
    x = 0 # of letters default
    for i in str.lower(): # looping throught the string
        if i in a_low: # check if character is in alphabet
            x = x + 1 # add to x for every letter in the string
    return x
    #print(f"{x} letters in string")

def sntct(str): # of sentences fn
    x = 0 # of sentences default
    if str[-1] != "." and str[-1] != "?" and str[-1] != "!": # check for punctuation at end of string
        str = f"{str}." # fix bad grammar for lazy people

    for i in str.lower():
        if i == "." or i == "?" or i == "!": # check for punctuation
            x = x + 1 # add to x for every sentence
    return x
    #print(f"{x} sentences in string")

    # graph functions
def hist(str): # histogram fn
    for l in a_low: # loop through alphabet
        x = 0 # define value of each letter

        for i in str.lower(): # loop through string
            if i == l: # check if the letter in the string is one of the letters in the alphabet
                x = x + 1 # add to letter's value
        print(f"{l}: {']' * x}") # print each letter and a "]" for every occurance in the string

def per(str): # percentage fn
    for l in a_low:
        x = 0

        for i in str.lower():
            if i == l:
                x = x + 1
        print(f"{l}: {round(100 * (x / charct(string)), 1)}%") # print each letter + value in %

while True:
    string = input("Enter a string of text (min 3 words please) ") # prompt user to enter some text
    from string import ascii_lowercase as a_low

    """for testing
    print(charct(string))
    print(wrdct(string))
    """
    if charct(string) < 1: # check if there are letters in string
        print("\nYou need to enter text in a TEXT ANALYSIS program but I'll just do it for you.")
        string = default_str # use default string
    elif wrdct(string) < 3: # make sure string has a few words
        print("\nI wasn't asking, enter 3 or more words.")
        continue
    
    print(string)
    print(f"\nYour string has {wrdct(string)} words, {charct(string)} letters, and {sntct(string)} sentences.")

    choice = input("\nEnter 1 for a histogram and 2 for percentages. Or 0 for neither. ") # prompt user with two choices, histogram or percentages

    if int(choice) == 1:
        hist(string) # run histogram function
        continue
    elif int(choice) == 2:
        per(string) # run percentage function
        continue
    else:
        print("Done") # end the text analysis
        break