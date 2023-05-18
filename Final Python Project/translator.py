# This program acts as a translator to eliminate language barriers
# It's function is to automatically detect, and translate diologue
# I am using an unofficial version of the google translate api for this through a library
# User 1 must speak english for now

# https://www.thepythoncode.com/article/translate-text-in-python
# https://hse.instructure.com/courses/133681/assignments/1271350

import json
import random
from googletrans import Translator, constants
translator = Translator()
autr = False

# Set variables
user_index = {
    "users": [
        {"name": "User 1", "language": "english"},
        {"name": "User 2", "language": ""}
    ]
}

# Create display
def user_interface():
    global autr

    print("======== Translator ========")

    while True:
        if autr == False: # Check if Auto-Translate is active or not
            print("\n________ MENU ________")
            print("1: Translate")
            print("2: Auto-Translate")
            print("3: Info")
            print("4: Print Conversation")
            print("0: Quit Translator\n")

            # Ask users choice 0-4
            choice = input("Make a selection: ")

            # Execute choice
            if choice == "1":
                print("\nWelcome to Translate!\n")
                translate()
            elif choice == "2":
                print("\nWelcome to Auto-Translate!\nTo exit say \"exit\".\n")
                autr = True
                autoTranslate()
            elif choice == "3":
                info()
            elif choice == "4":
                log(2)
            elif choice == "0":
                break
            else:
                print("Invalid Selection!")
        elif autr == True:
            autoTranslate()

# Convert ISO-639 code to language
def convert(ln):
    with open('Final Python Project/supported_languages.json') as fp:
        language_list = json.load(fp)

    ll = language_list["languages"]
    for i in ll:
        l = i["language"]
        c = i["code"]

        if c == ln:
            return l

# Translate a single basic string
def translate():
    u = user_index['users']
    
    ln = u[0]["language"]

    if ln == "":
        ln1 = (f"Language to translate: ")
    else:
        print(f"Your current language is {ln}.")
        ln1 = input(f"If you would like to use that don't enter anything, if not enter the language to translate or \"detect\" for language detection: ").lower()
        if ln1 == "":
            ln1 = ln
            print("Your current language will be used.")
        elif ln1 == "detect":
            print("The language will be detected.")
    ln2 = input("Language to translate to: ")
    text = input("Text to translate: ")

    if ln1 == "detect":
        ln = translator.detect(text)
        print(f"The language {convert(ln.lang)} was detected with a {ln.confidence * 100}% confidence.")
        ln1 = ln.lang
    try:
        translation = translator.translate(text, src=ln1, dest=ln2)
    except UnboundLocalError:
        print("There was an error running your translation. This is probably because one or more of your languages is invalid.\nTo change your language or to find a list of valid languages you can use Info in the menu.")
        return
    except ValueError:
        print("There was an error running your translation. This is probably because one or more of your languages is invalid.\nTo change your language or to find a list of valid languages you can use Info in the menu.")
        return
    tr = f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})"
    print(tr)

# Create messaging platform in terminal for Auto-Translate
def autoTranslate():
    global autr
    global user_index

    # Read user data
    u = user_index['users']

    if u[0]["language"] == "":
        print("You removed your language please add one in the menu using \"info.\"")
        autr = False
        return
    
    if u[1]["language"] == "": # Check if there is not already a language for User 2
        ln = input("What is the language of the person you are speaking to? (If you are unsure don't enter anything) ")
        if ln == "": # Check if a language was given
            print("Language will be auto detected after User 2 says something.")
        else:
            # Add given language
            user_index = {
                "users": [
                    {"name": "User 1", "language": "english"},
                    {"name": "User 2", "language": ln}
                ]
            }

        # Upload user index to Final Python Project/users.json
        with open('Final Python Project/users.json', 'w') as json_file:
            json.dump(user_index, json_file, indent=4, separators=(',',': '))
    
    with open('Final Python Project/users.json') as fp:
        users = json.load(fp)
    
    u = users['users']

    # Switch between users 1 and 2
    for i in range(2):
        # Check if there is a language for User 2
        if u[1]['language'] == "":
            if i == 0:
                text = input(f"{u[0]['name']}: ")
            elif i == 1:
                # Detect User 2's language by first message
                text = input(f"{u[1]['name']}: ")
                ln = translator.detect(text)

                # Add detected language
                user_index = {
                    "users": [
                        {"name": "User 1", "language": "english"},
                        {"name": "User 2", "language": convert(ln.lang).lower()}
                    ]
                }

                # Tell users which language was detected and how confident 
                print(f"The language {convert(ln.lang)} was detected with a {ln.confidence * 100}% confidence.")

                # Upload user index to Final Python Project/users.json
                with open('Final Python Project/users.json', 'w') as json_file:
                    json.dump(user_index, json_file, indent=4, separators=(',',': '))
                return
            # Check if user wants to end the conversation and go back to the menu
            if text.lower() == "exit":
                autr = False
                return
        # Use already known language 
        else:
            if i == 0:
                text = input(f"{u[0]['name']}: ")
                ln1 = u[0]['language']
                ln2 = u[1]['language']
            elif i == 1:
                text = input(f"{u[1]['name']}: ")
                ln1 = u[1]['language']
                ln2 = u[0]['language']
            # Check if user wants to end the conversation and go back to the menu
            if text.lower() == "exit":
                autr = False
                return
            else:
                # Randomly remind user how to exit
                if random.randint(0, 15) == 10:
                    print("Reminder: If you would like to exit Auto-Translate just say \"exit\".")
                
                # Translate text and log it
                try:
                    translation = translator.translate(text, src=ln1, dest=ln2)
                except UnboundLocalError:
                    print("There was an error running your translation. This is probably because one or more of your languages is invalid.\nTo change your language or to find a list of valid languages you can use Info in the menu.")
                    autr = False
                    return
                except ValueError:
                    print("There was an error running your translation. This is probably because one or more of your languages is invalid.\nTo change your language or to find a list of valid languages you can use Info in the menu.")
                    autr = False
                    return
                tr = f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})"
                print(tr)
            
            log(tr)

# Modify user data
def modify(x):
    global user_index

    # Reset the file
    if x == 1:
        user_index = {
            "users": [
                {"name": "User 1", "language": "english"},
                {"name": "User 2", "language": ""}
            ]
        }

        # Upload user index to Final Python Project/users.json
        with open('Final Python Project/users.json', 'w') as json_file:
            json.dump(user_index, json_file, indent=4, separators=(',',': '))

    elif x == 2:
        with open('Final Python Project/users.json') as fp:
            users = json.load(fp)
    
        u = users['users']

        u1n = u[0]["name"]
        u2n = u[1]["name"]
        u1l = u[0]["language"]
        u2l = u[1]["language"]

        # Ask what shoud be edited
        e1 = input("What would you like to edit? \"name\" for name \"language\" for language ")
        if e1.lower() != "name" and e1.lower() != "language": # Make sure e1 is a valid option
            print("Please enter a valid option.")
            return

        # Ask who should be edited
        e2 = input(f"Who would you like to edit? \"1\" for User 1 ({u1n}) \"2\" for User 2 ({u2n}) ")
        if e2 != "1" and e2 != "2": # Make sure e2 is a valid user
            print("Please enter a valid user number.")
            return

        # Check if name was chosen
        if e1.lower() == "name":
            nname = input(f"The new name for User {e2} is: ") # Ask for new name
            
            if e2 == "1": # If user 1:
                user_index = {
                    "users": [
                        {"name": nname, "language": u1l},
                        {"name": u2n, "language": u2l}
                    ]
                }
            
            elif e2 == "2": # If user 2
                user_index = {
                    "users": [
                        {"name": u1n, "language": u1l},
                        {"name": nname, "language": u2l}
                    ]
                }

        # Check if language was chosen
        elif e1.lower() == "language":
            nlang = input(f"The new language for User {e2} is: ") # Ask for new language
            
            if e2 == "1": # If user 1
                user_index = {
                    "users": [
                        {"name": u1n, "language": nlang},
                        {"name": u2n, "language": u2l}
                    ]
                }

            elif e2 == "2": # If user 2
                user_index = {
                    "users": [
                        {"name": u1n, "language": u1l},
                        {"name": u2n, "language": nlang}
                    ]
                }

        # Upload user index to Final Python Project/users.json
        with open('Final Python Project/users.json', 'w') as json_file:
            json.dump(user_index, json_file, indent=4, separators=(',',': '))

        # Show new modified data
        info()

# Display user data or languages
def info():
    global user_index

    with open('Final Python Project/users.json') as fp:
        user_list = json.load(fp)

    with open('Final Python Project/supported_languages.json') as fp:
        language_list = json.load(fp)
    
    u = user_list['users']
    ll = language_list["languages"]

    u1n = u[0]["name"]
    u2n = u[1]["name"]
    u1l = u[0]["language"]
    u2l = u[1]["language"]

    
    print("\n++++++++ Info ++++++++\n")
    # Ask the user what they want to know
    choice = input("What would you like to view? \"users\" for user data \"languages\" for a list of valid languages \"exit\" to exit ").lower()
    
    # Check if users was chosen
    if choice == "users":
        # Display current info if any
        print("***** User 1 *****")
        print(f"Name: {u[0]['name']}")
        print(f"Language: {u[0]['language']}\n")

        print("***** User 2 *****")
        print(f"Name: {u[1]['name']}")
        print(f"Language: {u[1]['language']}\n")
        
        # Check for complete user data
        if u1n != "" and u2n != "" and u1l != "" and u2l != "":
            # Ask if user would like to modify data
            if input("would you like to edit this? \"yes\" for yes \"no\" for no ").lower() == "yes":
                modify(2)
            else:
                return
        else:
            print("There is no or incomplete user data. You can try out Auto-Translate to automatically add information or you can manually add it.")
            # Ask user if they want to edit the data
            if input("would you like to manually add the info? \"yes\" for yes \"no\" for no ").lower() == "yes":
                modify(2)
            else:
                return
    # Check if languages was chosen
    elif choice == "languages":
        print("Language                    ISO-639")
        for i in ll:
            l = i["language"]
            c = i["code"]
            space = " " * (30 - len(l))
            print(f"{l}{space}{c}")

    # Check if exit was chosen
    elif choice == "exit":
        return
    
    # If invalid option
    else:
        print("Please enter a valid option.")
        return

# Access the Auto-Translate log
def log(x):
    # Reset the log
    if x == 1:
        with open('Final Python Project/autrlog.txt', 'w') as out_file:
            out_file.write("")

    # Display the log
    elif x == 2:
        with open('Final Python Project/autrlog.txt', 'r') as in_file:
            script = in_file.readlines()
            if len(script) < 1:
                print("Nothing to print yet. Try out Auto-Translate first and you can read the whole conversation here.")
            else:
                for i in script:
                    print(i)

    # Write to the log
    else:
        with open('Final Python Project/autrlog.txt', 'a') as out_file:
            out_file.write(f"{x}\n")   

# Reset log and user index and upload to json file for manual modifications to data
modify(1)
log(1)

# Run program
user_interface()