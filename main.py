dumb_word = ""
for letter in "supercalifragilisticexpialidocious":
    if letter > "m":
      continue
    dumb_word += letter
    print(dumb_word)