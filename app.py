import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
moves = open("./moves.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
move = json.load(moves)
# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
for pokemon in data:   
    name = pokemon["name"]["english"]
    print(name)

# Add a language choice feature and print the pokemons name based on the user input
language = input("Would you like to switch languages?: ")
if language.lower() == "yes":
    print("Select either Japanese, Chinese, or French.")
    choice = input("Enter a language: ")
    for pokemon in data:
        lang = pokemon["name"][f"{choice.lower()}"]
        print(lang)
if language.lower() == "no":
    choice = "english"

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
type = input("Would you like to find a type of pokemon?: ")
if type == "yes":
    select_type = input("Select a type: ").lower().capitalize()
    for pokemon in data:
        if select_type in pokemon["type"]:
            poketype = pokemon["name"][choice]
            print(poketype) 
if type == "no":
    print("Continue.")
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
find = input("Would you like to find a specific pokemon?: ")
find = find.lower()
if find == "yes":
    word = input("What pokemon do you want to find?:").lower().capitalize()
    for pokemon in data:
        if word in pokemon["name"]["english"]:
            name = pokemon["name"][f"{choice.lower()}"]
            print(name)
if find == "no":
    print ("Continue.")

#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
learn = input("Give a pokemon: ").lower().capitalize()
for pokemon in data:
    if learn == pokemon["name"]["english"]:
        poketype = pokemon["type"]
        for p in move:
            if p["type"] in poketype:
                thing = p["ename"]
                print(thing)