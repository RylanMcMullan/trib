import json

# Print list information in a way that looks good
def splitlist(list):
    for i in list:
        print(f"{i}, ")

# Open file with reading privlages
with open('Coding Assignments/pokedex/pokedex.json', 'r') as in_file:
    pokedex = json.load(in_file)

# Display all information
def user_interface():
    print("******** POKEDEX ********\n")

    while True:
        print("________ MENU ________")
        print("1: List all Pokemon")
        print("2: List Pokemon by type")
        print("3: Get a Pokemon")
        print("4: Get Pokemon evolutions")
        print("0: Quit")

        # Ask users choice 0-4
        choice = input("Make a selection: ")

        # Execute choice
        if choice == "1":
            list_all()
        elif choice == "2":
            list_by_type()
        elif choice == "3":
            display_pokemon()
        elif choice == "4":
            get_evolutions()
        elif choice == "0":
            break
        else:
            print("Invalid Selection!")

# List all pokemon
def list_all():
    print("\n")
    names = get_pokemon()
    # Run through all pokemon by number and value (name)
    for i, name in enumerate(names):
        print(f"{i + 1}: {name}")
    print("\n")

# List all pokemon of a certain type
def list_by_type():
    print("\n")
    # Request a pokemon type
    poke_type = input("Give a type: ")
    names = get_pokemon(poke_type)
    print(f"{poke_type} pokemon:")
    # Run through all pokemon of a certain type by number and value (name)
    for i, name in enumerate(names):
        print(f"{i + 1}: {name}")
    print("\n")

# Seach pokemon by name and display information about it
def display_pokemon():
    print("\n")
    names = get_pokemon()
    # Demand a pokemon name
    search = input("Give me a pokemon name ")
    for i, name in enumerate(names):
        # Look for searched pokemon
        if name == search:
            # Establish p as the pokemon
            p = pokedex['pokemon'][i]
            print(f"++++++++ {name} ++++++++\n")
            print(f"Type:")
            splitlist(p['type'])
            print(f"\nNumber: {p['num']}\n")
            print("Weaknesses:")
            splitlist(p['weaknesses'])
            print(f"\nHeight: {p['height']}")
            print(f"Weight: {p['weight']}\n")
            print(f"Spawn Chance: {p['spawn_chance']}")
            print(f"Spawn Time: {p['spawn_time']}")
    print("\n")

# Seach pokemon by name but only for evolutions
def get_evolutions():
    print("\n")
    names = get_pokemon()
    search = input("Give me a pokemon name ")
    for i, name in enumerate(names):
        if name == search:
            p = pokedex['pokemon'][i]
            print(f"++++++++ Evolutions ++++++++\n")
            # print seached pokemon in [id name] format
            print(f"{p['num']} {p['name']}")
            # print previous evolution in [id name] format
            print("Previous Evolution(s): ")
            try:
                # Run through all previous evolutions
                for i, value in enumerate(p['prev_evolution']):
                    print(f"{p['prev_evolution'][i]['num']} {p['prev_evolution'][i]['name']}")
            except:
                print("No previous evolutions.")
            # print next evolution in [id name] format
            print("Next Evolution(s): ")
            try:
                # Run through all future evolutions
                for i, value in enumerate(p['next_evolution']):
                    print(f"{p['next_evolution'][i]['num']} {p['next_evolution'][i]['name']}")
            except:
                print("Last evolution.")
    print("\n")

# Get all pokemon names from pokedex
def get_pokemon(type = "all"):
    # Check for type
    if type == "all":
        # Get all pokemon
        names = [p['name'] for p in pokedex['pokemon']]
    else:
        # Get all pokemon of a certain type
        names = [p['name'] for p in pokedex['pokemon'] if type in p['type']]

    return names

user_interface()