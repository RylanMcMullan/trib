### Finds all occurrances of a word in a set of text
### Write as a function that takes the text and the search term
### as input. Returns a list containing the indeces of all occurrances

# search for word in a string
def wrdsrch(str, srch):
    x = [] # list of each occurance of word
    string = str.lower().split(" ") # split string into individual words
    for count, value in enumerate(string): # get word (value) and it's index (count)
        if srch == value: #check if word is the searched word
            x.append(count) # add word to the list
    return x

sample_text = "It is not the critic who counts; not the man who points out how the strong man stumbles, or where the doer of deeds could have done them better. The credit belongs to the man who is actually in the arena, whose face is marred by dust and sweat an blood; who strives valiantly; who errs, who comes short again and again, because there is no effort without error and shortcoming; but who does actually strive to do the deeds; who knows great enthusiasms, the great devotions; who spends himself in a worthy cause; who at the best knows in the end the triumph of high achievement, and who at the worst, if he fails, at least fails while daringgreatly, so that his place shall never be with those cold and timid souls who neither know victory nor defeat."
search_term = ("man", "who", "and")

# print each word search
print(f"The word, {search_term[0]}, occurs {len(wrdsrch(sample_text, search_term[0]))} times.\n {wrdsrch(sample_text, search_term[0])}")
print(f"The word, {search_term[1]}, occurs {len(wrdsrch(sample_text, search_term[1]))} times.\n {wrdsrch(sample_text, search_term[1])}")
print(f"The word, {search_term[2]}, occurs {len(wrdsrch(sample_text, search_term[2]))} times.\n {wrdsrch(sample_text, search_term[2])}")
