# some_file.open("file_path", "mode")

# Modes
# r - read
# w - write
# r+ read and write
# a - append

with open("/Users/mcryr/Documents/GitHub/trib/bee_movie_script.txt", "a") as some_file:
    #x = some_file.read()
    #print(x)

    #x = some_file.readline(5)
    #print(x)
    #x = some_file.readline(6)
    #print(x)

    #print(list(some_file))

    #line = some_file.readline()
    #while line != '':
    #    print(line, end='')
    #    line = some_file.readline()

    some_file.write('Hello Class')
    some_file.write(' My name is Mr. Tribolet')
    some_file.writelines('\nI teach CS1.')

