import json


pokedex = {
    "Pokemon": [
        {"name": "Charmander", "type": "Fire", "level": 1, "evolution": "Charizard"},
        {"name": "Bulbasaur", "type": "Grass", "level": 3, "evolution": "Ivysaur"},
        {"name": "Squirtle", "type": "Water", "level": 5, "evolution": "Wartortle"}
    ]
}
with open("pokedex.json", "w") as file:
    json.dump(pokedex, file, indent=4)

with open("pokedex.json", "r") as file:
    data = json.load(file)

print(json.dumps(data, indent=4))