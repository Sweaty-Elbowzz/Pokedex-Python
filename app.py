import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
moves = open("./moves.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
move = json.load(moves)
# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
for i in range(0, 809):   
    name = data[i]["name"]["english"]
    print(name)

# Add a language choice feature and print the pokemons name based on the user input
language = input("Would you like to switch languages?: ")
if language.lower() == "yes":
    print("Select either Japanese, Chinese, or French.")
    choice = input("Enter a language: ")
    if choice.lower() == "japanese":
        for i in range(0, 809):
            print(data[i]["name"]["japanese"])
    elif choice.lower() == "chinese":
        for i in range(0, 809):
            print(data[i]["name"]["chinese"])
    elif choice.lower() == "french":
        for i in range(0, 809):
            print(data[i]["name"]["french"])
    else:
        print("Invalid language choice.")
if language.lower() == "no":
    choice = "english"

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
type = input("Would you like to find a type of pokemon?: ")
if type == "yes":
    select_type = input("Select a type: ")
    select_type = select_type.lower()
    select_type = select_type.capitalize()
    for t in range(0, 809):
        if select_type in data[t]["type"]:
            poketype = data[t]["name"][f"{choice}"]
            print(f"{t+1}: {poketype}") 
if type == "no":
    print("Continue.")
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
find = input("Would you like to find a specific pokemon?: ")
find = find.lower()
if find == "yes":
    word = input("What pokemon do you want to find?:")
    word = word.lower()
    word = word.capitalize()
    for f in range(0, 809):
        if word in data[f]["name"]["english"]:
            name = data[f]["name"][choice]
            print(f"{f+1}: {name}")
if find == "no":
    print ("Continue.")

#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
learn = input("Give a pokemon: ")
learn = learn.lower()
learn = learn.capitalize()
for l in range(0, 809):
    if learn == data[l]["name"]["english"]:
        pokemon_type = data[l]["type"]
        for p in range(0, len(move)):
            if move[p]["type"]:
                thing = move[p]["ename"]
                print(thing)